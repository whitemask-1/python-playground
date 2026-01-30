import os
from urllib import response
import requests
from datetime import datetime
from abc import ABC, abstractmethod
from dotenv import load_dotenv
import webbrowser
import time
from collections import defaultdict
import json
from pathlib import Path

#Rich Library for enhanced terminal output
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt, Confirm
from rich import box
from rich.progress import Progress, SpinnerColumn, TextColumn

# Initialize Rich console
console = Console()

load_dotenv()  # Load environment variables from .env file

"""
Rate Limiter tracks API usage to prevent quota exhaustion.

How it works:
- Each API call (fetch_top_stories or search_articles) increments the counter
- Rate limits are tracked per API source within rolling time windows
- Limits automatically reset after the specified time period
- Shared across all API instances to track total usage

Actions that count toward limits:
1. Fetching top stories (any section) = 1 call
2. Searching articles by keyword = 1 call  
3. Pagination (next/prev page) = 1 call per page
"""
class RateLimiter:
    def __init__(self):
        self.api_calls = defaultdict(list)  # Track calls per API
        self.limits = {
            # Format: 'api_key': {'calls': max_calls, 'period': seconds}
            'new york times': {'calls': 10, 'period': 60},  # 10 calls per minute
            'guardian': {'calls': 12, 'period': 1},   # 12 calls per second
            'newsapi.org': {'calls': 100, 'period': 86400},  # 100 per day (free tier)
            'gnews': {'calls': 100, 'period': 86400},    # 100 per day
            'mediastack': {'calls': 100, 'period': 2592000},  # 100 per month (free)
            'currents api': {'calls': 600, 'period': 86400}   # 600 per day
        }
        self.state_file = Path.home() / ".dailybugle" / "rate_limit_state.json"
        self._load_state()
    
    def _load_state(self):
        """Load saved rate limiter state from file"""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    data = json.load(f)
                    # Convert back to defaultdict with lists
                    self.api_calls = defaultdict(list, {
                        key: value for key, value in data.items()
                    })
                    # Clean up old calls on load
                    self._cleanup_old_calls()
            except (json.JSONDecodeError, IOError):
                pass
    
    def _save_state(self):
        """Save rate limiter state to file"""
        try:
            # Ensure directory exists
            self.state_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Clean up before saving
            self._cleanup_old_calls()
            
            # Convert defaultdict to regular dict for JSON
            state = dict(self.api_calls)
            
            with open(self.state_file, 'w') as f:
                json.dump(state, f, indent=2)
        except IOError as e:
            console.print(f"[yellow]Warning: Could not save rate limit state: {e}[/yellow]")
    
    def _cleanup_old_calls(self):
        """Remove expired calls from all APIs"""
        now = time.time()
        for api_key in list(self.api_calls.keys()):
            if api_key in self.limits:
                limit = self.limits[api_key]
                self.api_calls[api_key] = [
                    call_time for call_time in self.api_calls[api_key]
                    if now - call_time < limit['period']
                ]
                # Remove empty lists
                if not self.api_calls[api_key]:
                    del self.api_calls[api_key]
    
    def can_make_request(self, api_name):
        """Check if we can make a request without hitting rate limit"""
        api_key = api_name.lower()
        
        if api_key not in self.limits:
            return True  # No limit defined, allow request
        
        limit = self.limits[api_key]
        now = time.time()
        
        # Remove old calls outside the time window
        self.api_calls[api_key] = [
            call_time for call_time in self.api_calls[api_key]
            if now - call_time < limit['period']
        ]
        
        # Check if under limit
        if len(self.api_calls[api_key]) < limit['calls']:
            self.api_calls[api_key].append(now)
            self._save_state()  # ADD THIS: Save after each call
            return True
        
        return False
    
    def time_until_reset(self, api_name):
        """Get seconds until rate limit resets"""
        api_key = api_name.lower()
        
        if api_key not in self.limits or not self.api_calls[api_key]:
            return 0
        
        limit = self.limits[api_key]
        oldest_call = min(self.api_calls[api_key])
        reset_time = oldest_call + limit['period']
        
        return max(0, reset_time - time.time())
    
    def get_remaining_calls(self, api_name):
        """Get number of remaining API calls available"""
        api_key = api_name.lower()
        
        if api_key not in self.limits:
            return float('inf')  # Unlimited
        
        limit = self.limits[api_key]
        now = time.time()
        
        # Remove old calls
        self.api_calls[api_key] = [
            call_time for call_time in self.api_calls[api_key]
            if now - call_time < limit['period']
        ]
        
        return limit['calls'] - len(self.api_calls[api_key])
    
    def get_all_api_status(self):
        """Get rate limit status for all APIs"""
        status = {}
        for api_key, limit in self.limits.items():
            remaining = self.get_remaining_calls(api_key)
            time_to_reset = self.time_until_reset(api_key)
            
            status[api_key] = {
                'limit': limit['calls'],
                'remaining': remaining if remaining != float('inf') else 'unlimited',
                'reset_in': time_to_reset,
                'period': limit['period']
            }
        
        return status

#Article Class
class Article:
    def __init__(self, title, abstract, byline, url, published_date, section=None, source=None):
        self.title = title
        self.abstract = abstract
        self.byline = byline
        self.url = url
        self.published_date = published_date
        self.section = section
        self.source = source
        self.full_details = None
        self.fetched_at = datetime.now()
    
    def __str__(self): #Display basic article info
        """Display basic article info with rich formatting"""
        source_tag = f" [{self.source}]" if self.source else ""
        
        # Create a panel with the article
        content = Text()
        content.append(f"{self.title}", style="bold cyan")
        content.append(source_tag, style="dim")
        content.append(f"\n\n{self.byline}", style="italic yellow")
        content.append(f"\n{self.published_date}", style="dim")
        content.append(f"\n\n{self.abstract}", style="white")
        
        panel = Panel(
            content,
            border_style="blue",
            box=box.ROUNDED,
            padding=(1, 2)
        )
        
        # Return string representation for printing
        from io import StringIO
        string_io = StringIO()
        temp_console = Console(file=string_io, force_terminal=True)
        temp_console.print(panel)
        return string_io.getvalue()
    
    def display_full_details(self): #Display comprehensive article information
        if not self.full_details or not isinstance(self.full_details, dict): #If there are no details
            return "Full details not available."
        
        output = f"\n{'='*80}\n"
        output += f"TITLE: {self.title}\n"
        output += f"{'-'*80}\n"
        output += f"BYLINE: {self.byline}\n"
        output += f"PUBLISHED: {self.published_date}\n"
        output += f"SECTION: {self.section}\n"
        output += f"SOURCE: {self.source}\n"
        output += f"URL: {self.url}\n"
        output += f"{'-'*80}\n"
        output += f"ABSTRACT:\n{self.abstract}\n"

        if self.full_details.get('lead_paragraph'): #If theres a lead paragraph then use it
            output += f"\nLEAD PARAGRAPH:\n{self.full_details['lead_paragraph']}\n"
        
        if self.full_details.get('snippet'): #If theres a snippet then use it
            output += f"\nSNIPPET:\n{self.full_details['snippet']}\n"

        output += f"{'='*80}\n"
        return output

    def to_dict(self): #Convert article to dictionary format for JSON serialization
        return {
            'title': self.title,
            'abstract': self.abstract,
            'byline': self.byline,
            'url': self.url,
            'published_date': self.published_date,
            'section': self.section,
            'full_details': self.full_details,
            'fetched_at': self.fetched_at.isoformat() #ISO format for datetime ex. 2024-06-10T14:48:00
        }
    
class NewsAPI(ABC):
    #Shared rate limiter across all API instances
    _shared_rate_limiter = RateLimiter()    

    def __init__(self):
        self.api_name = "Generic News API"
        self.api_key = None
        self.rate_limiter = NewsAPI._shared_rate_limiter
    
    def _check_rate_limit(self):
        """Check rate limit before making request"""
        if not self.rate_limiter.can_make_request(self.api_name):
            wait_time = int(self.rate_limiter.time_until_reset(self.api_name))
            
            if wait_time > 3600:  # More than 1 hour
                hours = wait_time // 3600
                raise ConnectionError(
                    f"⚠️  Rate limit reached for {self.api_name}.\n"
                    f"Please wait {hours} hour(s) before trying again."
                )
            elif wait_time > 60:  # More than 1 minute
                minutes = wait_time // 60
                raise ConnectionError(
                    f"⚠️  Rate limit reached for {self.api_name}.\n"
                    f"Please wait {minutes} minute(s) before trying again."
                )
            else:
                raise ConnectionError(
                    f"⚠️  Rate limit reached for {self.api_name}.\n"
                    f"Please wait {wait_time} seconds before trying again."
                )

    @abstractmethod
    def fetch_top_stories(self, section='home', page=1):
        # Abstract method to fetch top stories
        pass

    @abstractmethod
    def search_articles(self, query, page=1):
        # Abstract method to search articles
        pass

    @abstractmethod
    def get_available_sections(self):
        # Abstract method to get available sections
        pass

    def get_api_name(self): #Return API name
        return self.api_name
    
# NY Times API Interaction Class to handle all API requests
class NYTimesAPI(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_key = os.getenv('NYTIMES_API_KEY') #Get API key from environment variable
        if not self.api_key:
            raise ValueError("NYTIMES_API_KEY not found in environment variables.")
        self.api_name = "The New York Times"
        self.top_stories_base_url = "https://api.nytimes.com/svc/topstories/v2"
        self.article_search_base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
        
        # Available sections for Top Stories API
    def get_available_sections(self):
        return [
            'home', 'arts', 'automobiles', 'books', 'business', 
            'fashion', 'food', 'health', 'insider', 'magazine',
            'movies', 'nyregion', 'obituaries', 'opinion', 'politics',
            'realestate', 'science', 'sports', 'sundayreview', 
            'technology', 'theater', 't-magazine', 'travel', 'upshot', 'us', 'world'
        ]

    def fetch_top_stories(self, section='home', page=1): #Fetch top stories from NY Times Top Stories API
        self._check_rate_limit()  # Check rate limit before making request
        try: #Try calling the API
            url = f"{self.top_stories_base_url}/{section}.json" #Set URL for top stories endpoint
            params = {'api-key': self.api_key} #Set parameters with API key

            response = requests.get(url, params=params) #Make GET request to NY Times API
            response.raise_for_status() #Raise error for bad responses

            data = response.json() #Parse JSON response
            articles = [] #List to hold articles

            for item in data.get('results', [])[:20]: #Limit to 20 stories
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('abstract', 'No Abstract'),
                    byline=item.get('byline', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('published_date', ''),
                    section=item.get('section', section),
                    source=self.api_name
                )
                articles.append(article) #Add article to list
        
            return articles #Return list of articles

        except requests.RequestException as e: #Handle request exceptions
            raise ConnectionError(f"Failed to fetch top stories: {e}")
    
    def search_articles(self, query, section=None, begin_date=None, page=1):
        self._check_rate_limit()  # Check rate limit before making request
        """Search for articles using Article Search API"""
        try:
            params = {
                'api-key': self.api_key,
                'q': query,  # Search query
                'sort': 'newest',
                'page': page - 1  # NYT API uses 0-based page indexing
            }
            
            # Add section filter if provided
            if section:
                params['fq'] = f'section_name:("{section}")'
            
            # Add date filter if provided
            if begin_date:
                params['begin_date'] = begin_date  # Format: YYYYMMDD
            
            response = requests.get(self.article_search_base_url, params=params)
            response.raise_for_status()

            data = response.json()
            docs = data.get('response', {}).get('docs', [])
            
            articles = []
            for doc in docs[:20]:  # Limit to 20 results
                article = Article(
                    title=doc.get('headline', {}).get('main', 'Untitled'),
                    abstract=doc.get('abstract', 'No abstract available'),
                    byline=doc.get('byline', {}).get('original', 'Unknown Author'),
                    url=doc.get('web_url', ''),
                    published_date=doc.get('pub_date', ''),
                    section=doc.get('section_name', ''),
                    source=self.api_name
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search articles: {e}")
        
class GuardianAPI(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_name = "The Guardian"
        self.api_key = os.getenv('GUARDIAN_API_KEY')
        if not self.api_key:
            raise ValueError("GUARDIAN_API_KEY not found in environment variables.")
        
        self.base_url = "https://content.guardianapis.com"

    def get_available_sections(self):
        return [
            'world', 'uk-news', 'politics', 'business', 'technology',
            'science', 'environment', 'sport', 'culture', 'books',
            'music', 'film', 'tv-and-radio', 'artanddesign', 'fashion',
            'food', 'travel', 'lifeandstyle', 'money', 'education'
        ]

    def fetch_top_stories(self, section='world', page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/search"
            params = {
                'api-key': self.api_key,
                'section': section,
                'show-fields': 'byline,trailText',
                'order-by': 'newest',
                'page-size': 20,
                'page': page
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            articles = []

            for item in data.get('response', {}).get('results', []):
                article = Article(
                    title=item.get('webTitle', 'Untitled'),
                    abstract=item.get('fields', {}).get('trailText', 'No abstract available'),
                    byline=item.get('fields', {}).get('byline', 'The Guardian'),
                    url=item.get('webUrl', ''),
                    published_date=item.get('webPublicationDate', ''),
                    section=item.get('sectionName', section),
                    source=self.api_name
                )
                articles.append(article)
        
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to fetch top stories from {self.api_name}: {e}")
    
    def search_articles(self, query, page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/search"
            params = {
                'api-key': self.api_key,
                'q': query,
                'show-fields': 'byline,trailText',
                'order-by': 'relevance',
                'page-size': 20,
                'page': page
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            articles = []
            
            for item in data.get('response', {}).get('results', []):
                article = Article(
                    title=item.get('webTitle', 'Untitled'),
                    abstract=item.get('fields', {}).get('trailText', 'No abstract available'),
                    byline=item.get('fields', {}).get('byline', 'The Guardian'),
                    url=item.get('webUrl', ''),
                    published_date=item.get('webPublicationDate', ''),
                    section=item.get('sectionName', ''),
                    source=self.api_name
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search articles from {self.api_name}: {e}")

# ==================== NewsAPI.org Implementation ====================
class NewsAPIOrg(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_name = "NewsAPI.org"
        self.api_key = os.getenv('NEWSAPI_API_KEY')
        if not self.api_key:
            raise ValueError("NEWSAPI_API_KEY not found in environment variables.")
        
        self.base_url = "https://newsapi.org/v2"

    def get_available_sections(self):
        return [
            'business', 'entertainment', 'general', 'health',
            'science', 'sports', 'technology'
        ]

    def fetch_top_stories(self, section='general', page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/top-headlines"
            params = {
                'apiKey': self.api_key,
                'category': section,
                'country': 'us',  # Can be made configurable
                'pageSize': 20,
                'page': page
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if data.get('status') != 'ok':
                raise ConnectionError(f"API returned error: {data.get('message')}")
            
            articles = []
            for item in data.get('articles', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('publishedAt', ''),
                    section=section,
                    source=f"{self.api_name} - {item.get('source', {}).get('name', 'Unknown')}"
                )
                articles.append(article)
        
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to fetch from {self.api_name}: {e}")
    
    def search_articles(self, query, page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/everything"
            params = {
                'apiKey': self.api_key,
                'q': query,
                'sortBy': 'publishedAt',
                'language': 'en',
                'pageSize': 20,
                'page': page
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if data.get('status') != 'ok':
                raise ConnectionError(f"API returned error: {data.get('message')}")
            
            articles = []
            for item in data.get('articles', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('publishedAt', ''),
                    section='search',
                    source=f"{self.api_name} - {item.get('source', {}).get('name', 'Unknown')}"
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search {self.api_name}: {e}")


# ==================== GNews API Implementation ====================
class GNewsAPI(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_name = "GNews"
        self.api_key = os.getenv('GNEWS_API_KEY')
        if not self.api_key:
            raise ValueError("GNEWS_API_KEY not found in environment variables.")
        
        self.base_url = "https://gnews.io/api/v4"

    def get_available_sections(self):
        return [
            'general', 'world', 'nation', 'business', 'technology',
            'entertainment', 'sports', 'science', 'health'
        ]

    def fetch_top_stories(self, section='general'):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/top-headlines"
            params = {
                'token': self.api_key,
                'topic': section,
                'lang': 'en',
                'country': 'us',
                'max': 20
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            articles = []

            for item in data.get('articles', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('source', {}).get('name', 'Unknown Source'),
                    url=item.get('url', ''),
                    published_date=item.get('publishedAt', ''),
                    section=section,
                    source=self.api_name
                )
                articles.append(article)
        
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to fetch from {self.api_name}: {e}")
    
    def search_articles(self, query):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/search"
            params = {
                'token': self.api_key,
                'q': query,
                'lang': 'en',
                'max': 20,
                'sortby': 'publishedAt'
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            articles = []
            
            for item in data.get('articles', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('source', {}).get('name', 'Unknown Source'),
                    url=item.get('url', ''),
                    published_date=item.get('publishedAt', ''),
                    section='search',
                    source=self.api_name
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search {self.api_name}: {e}")


# ==================== Mediastack API Implementation ====================
class MediastackAPI(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_name = "Mediastack"
        self.api_key = os.getenv('MEDIASTACK_API_KEY')
        if not self.api_key:
            raise ValueError("MEDIASTACK_API_KEY not found in environment variables.")
        
        self.base_url = "http://api.mediastack.com/v1"

    def get_available_sections(self):
        return [
            'general', 'business', 'entertainment', 'health',
            'science', 'sports', 'technology'
        ]

    def fetch_top_stories(self, section='general', page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/news"
            params = {
                'access_key': self.api_key,
                'categories': section,
                'languages': 'en',
                'countries': 'us',
                'limit': 20,
                'sort': 'published_desc',
                'page': (page-1)*20
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if 'error' in data:
                raise ConnectionError(f"API error: {data['error'].get('message')}")
            
            articles = []
            for item in data.get('data', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('published_at', ''),
                    section=item.get('category', section),
                    source=f"{self.api_name} - {item.get('source', 'Unknown')}"
                )
                articles.append(article)
        
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to fetch from {self.api_name}: {e}")
    
    def search_articles(self, query, page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/news"
            params = {
                'access_key': self.api_key,
                'keywords': query,
                'languages': 'en',
                'limit': 20,
                'sort': 'published_desc',
                'page': (page-1)*20
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if 'error' in data:
                raise ConnectionError(f"API error: {data['error'].get('message')}")
            
            articles = []
            for item in data.get('data', []):
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('published_at', ''),
                    section=item.get('category', 'search'),
                    source=f"{self.api_name} - {item.get('source', 'Unknown')}"
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search {self.api_name}: {e}")


# ==================== Currents API Implementation ====================
class CurrentsAPI(NewsAPI):
    def __init__(self):
        super().__init__()
        self.api_name = "Currents API"
        self.api_key = os.getenv('CURRENTS_API_KEY')
        if not self.api_key:
            raise ValueError("CURRENTS_API_KEY not found in environment variables.")
        
        self.base_url = "https://api.currentsapi.services/v1"

    def get_available_sections(self):
        return [
            'regional', 'technology', 'lifestyle', 'business',
            'general', 'programming', 'science', 'entertainment',
            'world', 'sports', 'finance', 'academia', 'politics',
            'health', 'opinion', 'food', 'game'
        ]

    def fetch_top_stories(self, section='general', page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/latest-news"
            params = {
                'apiKey': self.api_key,
                'category': section,
                'language': 'en',
                'page': page
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if data.get('status') != 'ok':
                raise ConnectionError(f"API error: {data.get('message')}")
            
            articles = []
            for item in data.get('news', [])[:20]:
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('published', ''),
                    section=section,
                    source=self.api_name
                )
                articles.append(article)
        
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to fetch from {self.api_name}: {e}")
    
    def search_articles(self, query, page=1):
        self._check_rate_limit()  # Check rate limit before making request
        try:
            url = f"{self.base_url}/search"
            params = {
                'apiKey': self.api_key,
                'keywords': query,
                'language': 'en',
                'page': page
            }
            
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()
            
            if data.get('status') != 'ok':
                raise ConnectionError(f"API error: {data.get('message')}")
            
            articles = []
            for item in data.get('news', [])[:20]:
                article = Article(
                    title=item.get('title', 'Untitled'),
                    abstract=item.get('description', 'No description available'),
                    byline=item.get('author', 'Unknown Author'),
                    url=item.get('url', ''),
                    published_date=item.get('published', ''),
                    section='search',
                    source=self.api_name
                )
                articles.append(article)
            
            return articles

        except requests.RequestException as e:
            raise ConnectionError(f"Failed to search {self.api_name}: {e}")

class NewsArchive: # Archive Management Class
    def __init__(self):
        self.archive = [] #Directory to store archived news

    def add_to_archive(self, article): #Add article to archive
        if not isinstance(article, Article):
            raise TypeError("Only Article objects can be archived.")
        self.archive.append(article)
    
    def __len__(self): #Get number of archived articles
        return len(self.archive)
    
    def __str__(self): #String representation of the archive
        return f"News Archive: {len(self.archive)} articles stored."
    
    def display_all(self): #Display all archived articles
        if not self.archive:
            print("Archive is empty.")
            return
        
        for i, article in enumerate(self.archive, start=1):
            print(f"\n{i}. {article.title} - {article.published_date} by {article.byline}")
            print(article)

class DailyBugleMenu:
    def __init__(self):
        self.archive = NewsArchive()
        self.current_stories = []
        self.current_page = 1 
        self.current_mode = None 
        self.current_section = None  
        self.current_query = None  
        self.scheduled = False
        self.available_apis = {}
        self.current_api = None

        self.config_dir = Path.home() / ".dailybugle"
        self.config_file = self.config_dir / "config.json"
        self.config_dir.mkdir(parents=True, exist_ok=True)
        
        self._register_apis()
        self._load_config()

        # Dictionary dispatch for menu options
        self.menu_actions = {
            '0': self.select_api_source,
            '1': self.view_todays_stories,
            '2': self.browse_by_section,
            '3': self.search_articles,
            '4': self.view_old_archives,
            '5': self.view_rate_limits,  
            '6': self.exit_program  
        }
    
    def _load_config(self):
        """Load saved configuration from file"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    saved_api_key = config.get('current_api')
                    
                    # Set current API based on saved preference
                    if saved_api_key and saved_api_key in self.available_apis:
                        self.current_api = self.available_apis[saved_api_key]
                        print(f"✓ Loaded saved preference: {self.current_api.get_api_name()}")
                    else:
                        self._set_default_api()
            except (json.JSONDecodeError, IOError):
                self._set_default_api()
        else:
            self._set_default_api()

    def _set_default_api(self):
        """Set default API if no config exists"""
        if self.available_apis:
            self.current_api = list(self.available_apis.values())[0]
            print(f"\nDefault source: {self.current_api.get_api_name()}")
    
    def _save_config(self):
        """Save current configuration to file"""
        # Find the key for current API
        current_api_key = None
        for key, api in self.available_apis.items():
            if api == self.current_api:
                current_api_key = key
                break
        
        config = {
            'current_api': current_api_key,
            'last_updated': datetime.now().isoformat()
        }
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
        except IOError as e:
            print(f"Warning: Could not save config: {e}")

    def _register_apis(self):
        """Register all available news APIs"""
        apis_to_register = [
            ('nytimes', NYTimesAPI),
            ('guardian', GuardianAPI),
            ('newsapi', NewsAPIOrg),
            ('gnews', GNewsAPI),
            ('mediastack', MediastackAPI),
            ('currents', CurrentsAPI)
        ]
        
        for key, api_class in apis_to_register:
            try:
                api_instance = api_class()
                self.available_apis[key] = api_instance
                print(f"✓ {api_instance.get_api_name()} API loaded")
            except ValueError as e:
                print(f"✗ {api_class.__name__} not available: {e}")
        
        # Set default API if any available
        if self.available_apis:
            self.current_api = list(self.available_apis.values())[0]
            print(f"\nDefault source: {self.current_api.get_api_name()}")

    def select_api_source(self):
        """Select API source with rich formatting"""
        if not self.available_apis:
            console.print("[red]No news APIs are available. Please check your configuration.[/red]")
            return
        
        console.print()
        console.print(Panel("Available News APIs", style="bold cyan"))
        
        # Create API selection table
        table = Table(show_header=True, box=box.ROUNDED)
        table.add_column("#", style="cyan", width=6)
        table.add_column("API Source", style="yellow")
        table.add_column("Status", style="green")
        
        api_list = list(self.available_apis.items())
        for i, (key, api) in enumerate(api_list, start=1):
            current_marker = "✓ CURRENT" if api == self.current_api else ""
            table.add_row(str(i), api.get_api_name(), current_marker)
        
        console.print(table)
        
        choice = Prompt.ask(
            f"\n[bold cyan]Select API[/bold cyan] [dim](1-{len(api_list)} or 'q' to cancel)[/dim]",
            default="q"
        )
        
        if choice.lower() == 'q':
            return
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(api_list):
                self.current_api = api_list[index][1]
                self._save_config()
                console.print(f"[green]✓[/green] Current API set to: [bold]{self.current_api.get_api_name()}[/bold]")
                console.print("[green]✓[/green] Preference saved for next session")
            else:
                console.print("[red]Invalid selection. Please try again.[/red]")
        except ValueError:
            console.print("[red]Please enter a valid number or 'q' to cancel.[/red]")
    
    def browse_by_section(self):
        """Browse stories by specific section with rich formatting"""
        console.print()
        console.print(Panel("Available Sections", style="bold cyan"))
        
        # Display sections in a table
        sections = self.current_api.get_available_sections()
        table = Table(show_header=False, box=None, padding=(0, 2))
        
        # Create columns dynamically
        cols = 3
        for _ in range(cols):
            table.add_column(style="yellow")
        
        # Add rows
        for i in range(0, len(sections), cols):
            row = sections[i:i+cols]
            # Pad with empty strings if needed
            while len(row) < cols:
                row.append("")
            table.add_row(*row)
        
        console.print(table)
        
        section = Prompt.ask(
            "\n[bold cyan]Enter section name[/bold cyan] [dim](or 'q' to cancel)[/dim]"
        ).lower()
        
        if section == 'q':
            return
        
        if section not in self.current_api.get_available_sections():
            console.print(f"[red]Invalid section. Please choose from the list above.[/red]")
            return
        
        self.current_mode = 'section'
        self.current_section = section
        self.current_page = 1
        self._fetch_and_display_stories()
    
    def view_todays_stories(self):
        """View top stories from home section"""

        if not self.current_api:
            print("\nNo news source selected.")
            return
    
        self.current_mode = 'top_stories'
        self.current_page = 1
        self._fetch_and_display_stories()

    def browse_by_section(self):
        """Browse stories by specific section"""
        print("\n" + "="*60)
        print("AVAILABLE SECTIONS")
        print("="*60)
        
        # Display sections in columns
        sections = self.current_api.get_available_sections()
        for i in range(0, len(sections), 3):
            row = sections[i:i+3]
            print("  ".join(f"{s:20}" for s in row))
        
        print("="*60)
        
        section = input("\nEnter section name (or 'q' to cancel): ").lower()
        
        if section == 'q':
            return
        
        if section not in self.current_api.get_available_sections():
            print(f"Invalid section. Please choose from the list above.")
            return
        
        self.current_mode = 'section'
        self.current_section = section
        self.current_page = 1
        self._fetch_and_display_stories()

    def _fetch_and_display_stories(self):
        """Fetch and display stories with rich progress indicator"""
        try:
            # Show loading spinner
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                transient=True,
            ) as progress:
                if self.current_mode == 'top_stories':
                    progress.add_task(f"Fetching top stories (Page {self.current_page})...", total=None)
                    self.current_stories = self.current_api.fetch_top_stories(page=self.current_page)
                elif self.current_mode == 'section':
                    progress.add_task(f"Fetching {self.current_section} stories (Page {self.current_page})...", total=None)
                    self.current_stories = self.current_api.fetch_top_stories(self.current_section, page=self.current_page)
                elif self.current_mode == 'search':
                    progress.add_task(f"Searching '{self.current_query}' (Page {self.current_page})...", total=None)
                    self.current_stories = self.current_api.search_articles(self.current_query, page=self.current_page)

            if not self.current_stories:
                console.print("[yellow]No stories available.[/yellow]")
                return
        
            self._display_and_interact_with_stories()
        except ConnectionError as e:
            console.print(f"[red]Error: {e}[/red]")

    def search_articles(self):
        """Search for articles with rich formatting"""
        query = Prompt.ask("\n[bold cyan]Enter search keywords[/bold cyan]")
        
        if not query.strip():
            console.print("[red]Search query cannot be empty.[/red]")
            return
        
        self.current_mode = 'search'
        self.current_query = query
        self.current_page = 1
        self._fetch_and_display_stories()

    def _display_and_interact_with_stories(self):
        """Helper method to display stories with rich formatting"""
        console.print()
        console.print(Panel(
            f"[bold]Page {self.current_page}[/bold] - Found [green]{len(self.current_stories)}[/green] stories",
            style="cyan"
        ))
        console.print()
        
        # Create stories table
        table = Table(show_header=True, box=box.ROUNDED, border_style="cyan")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Title", style="bold yellow", overflow="fold")
        table.add_column("Details", style="dim", width=40)
        
        for i, article in enumerate(self.current_stories, start=1):
            details = f"{article.byline}\n{article.section}"
            table.add_row(
                str(i),
                article.title,
                details
            )
        
        console.print(table)
        
        while True:
            console.print()
            console.print("[dim]Options:[/dim] [cyan][number][/cyan]=view | [cyan]n[/cyan]=next page | [cyan]p[/cyan]=prev page | [cyan]q[/cyan]=quit")
            choice = Prompt.ask("[bold cyan]Your choice[/bold cyan]").lower()
        
            if choice == 'q':
                break
            elif choice == 'n':
                self.current_page += 1
                self._fetch_and_display_stories()
                break
            elif choice == 'p':
                if self.current_page > 1:
                    self.current_page -= 1
                    self._fetch_and_display_stories()
                    break
                else:
                    console.print("[yellow]Already on first page.[/yellow]")
            else:
                try:
                    index = int(choice) - 1
                    if 0 <= index < len(self.current_stories):
                        selected_article = self.current_stories[index]
                        console.print(selected_article)
                    
                        if Confirm.ask("\n[bold cyan]Open in browser?[/bold cyan]"):
                            webbrowser.open(selected_article.url)
                            console.print("[green]✓[/green] Opened in browser")
                    
                        if Confirm.ask("\n[bold cyan]Archive this article?[/bold cyan]"):
                            self.archive.add_to_archive(selected_article)
                            console.print(f"[green]✓[/green] Archived! Total: [bold]{len(self.archive)}[/bold]")
                    else:
                        console.print("[red]Invalid article number.[/red]")
                except ValueError:
                    console.print("[red]Invalid input.[/red]")

    def view_old_archives(self):
        """View all archived articles with rich formatting"""
        console.print()
        console.print(Panel("Archived Articles", style="bold cyan"))
        
        if not self.archive.archive:
            console.print("[yellow]No articles in archive.[/yellow]")
            return
        
        # Create archive table
        table = Table(show_header=True, box=box.ROUNDED, border_style="cyan")
        table.add_column("#", style="cyan", width=4)
        table.add_column("Title", style="bold yellow", overflow="fold")
        table.add_column("Archived", style="dim", width=20)
        
        for i, article in enumerate(self.archive.archive, start=1):
            table.add_row(
                str(i),
                article.title,
                article.fetched_at.strftime('%Y-%m-%d %I:%M %p')
            )
        
        console.print(table)
        
        while True:
            choice = Prompt.ask(
                "\n[bold cyan]Enter article number to view[/bold cyan] [dim](or 'q' to return)[/dim]",
                default="q"
            )
            
            if choice.lower() == 'q':
                break

            try: 
                index = int(choice) - 1
                if 0 <= index < len(self.archive.archive):
                    selected_article = self.archive.archive[index]
                    console.print(selected_article)
                    
                    if Confirm.ask("\n[bold cyan]Open in browser?[/bold cyan]"):
                        webbrowser.open(selected_article.url)
                        console.print("[green]✓[/green] Opened in browser")
                else:
                    console.print("[red]Invalid article number.[/red]")
            except ValueError:
                console.print("[red]Please enter a valid number or 'q' to return.[/red]")
    
    def exit_program(self):
        """Exit the application"""
        self._save_config()
        # Save rate limiter state on exit
        if self.current_api:
            self.current_api.rate_limiter._save_state()
        console.print("\n[bold yellow]Exiting the Daily Bugle News System. Goodbye![/bold yellow] 👋\n")
        return False
    
    def view_rate_limits(self):
        """View rate limit status for all APIs"""
        console.print()
        console.print(Panel("API Rate Limit Status", style="bold cyan"))
        
        # Get status for all APIs
        status = NewsAPI._shared_rate_limiter.get_all_api_status()
        
        # Create status table
        table = Table(show_header=True, box=box.ROUNDED, border_style="cyan")
        table.add_column("API", style="yellow", width=20)
        table.add_column("Limit", style="cyan", justify="right", width=10)
        table.add_column("Remaining", style="green", justify="right", width=12)
        table.add_column("Reset In", style="magenta", justify="right", width=12)
        
        for api_name, info in status.items():
            # Format reset time
            reset_time = info['reset_in']
            if reset_time == 0:
                reset_str = "N/A"
            elif reset_time > 3600:
                reset_str = f"{int(reset_time / 3600)}h"
            elif reset_time > 60:
                reset_str = f"{int(reset_time / 60)}m"
            else:
                reset_str = f"{int(reset_time)}s"
            
            # Color code remaining calls
            remaining = info['remaining']
            if remaining == 'unlimited':
                remaining_str = "[green]∞[/green]"
            elif remaining == 0:
                remaining_str = "[red]0[/red]"
            elif remaining < info['limit'] * 0.2:  # Less than 20%
                remaining_str = f"[red]{remaining}[/red]"
            elif remaining < info['limit'] * 0.5:  # Less than 50%
                remaining_str = f"[yellow]{remaining}[/yellow]"
            else:
                remaining_str = f"[green]{remaining}[/green]"
            
            table.add_row(
                api_name.title(),
                str(info['limit']),
                remaining_str,
                reset_str
            )
        
        console.print(table)
        console.print("\n[dim]Press Enter to return to menu...[/dim]")
        input()
    
    def display_menu(self):
        """Display main menu with rich formatting"""
        console.print("\n")
        
        # Create title panel
        title = Text("DAILY BUGLE NEWS SYSTEM", style="bold yellow", justify="center")
        console.print(Panel(title, border_style="cyan", box=box.DOUBLE))
        
        # Show current API and rate limit info
        if self.current_api:
            remaining = self.current_api.rate_limiter.get_remaining_calls(self.current_api.get_api_name())
            time_to_reset = self.current_api.rate_limiter.time_until_reset(self.current_api.get_api_name())
            
            if remaining == float('inf'):
                limit_info = "unlimited calls"
            else:
                limit_info = f"{int(remaining)} calls remaining"
                if time_to_reset > 0:
                    if time_to_reset > 3600:
                        reset_str = f"{int(time_to_reset / 3600)}h"
                    elif time_to_reset > 60:
                        reset_str = f"{int(time_to_reset / 60)}m"
                    else:
                        reset_str = f"{int(time_to_reset)}s"
                    limit_info += f" (resets in {reset_str})"
            
            info_text = Text()
            info_text.append("Current Source: ", style="dim")
            info_text.append(f"{self.current_api.get_api_name()}", style="bold green")
            info_text.append(f" ({limit_info})", style="dim cyan")
            console.print(info_text)
        
        console.print()
        
        # Create menu table
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_column("Option", style="bold cyan", width=8)
        table.add_column("Description", style="white")
        
        table.add_row("0", "🔌 Select News API Source")
        table.add_row("1", "📰 View Today's Top Stories")
        table.add_row("2", "📚 Browse Stories by Section")
        table.add_row("3", "🔍 Search Articles by Keyword")
        table.add_row("4", "📦 View Archived Articles")
        table.add_row("5", "📊 View Rate Limit Status")  # ADD THIS
        table.add_row("6", "🚪 Exit")  # CHANGE FROM 5
        
        console.print(table)
        console.print()
    
    def invalid_choice(self):
        """Handle invalid menu choices"""
        console.print("[red]Invalid choice. Please enter a number between 0-6.[/red]")  # CHANGE TO 0-6
    
    def run(self):
        """Main application loop"""
        # Welcome banner
        welcome = Text("Welcome to the Daily Bugle News System!", style="bold yellow", justify="center")
        subtitle = Text("Stay informed with the latest headlines and stories", style="dim", justify="center")
        
        console.print()
        console.print(Panel.fit(
            Text.assemble(welcome, "\n", subtitle),
            border_style="cyan",
            box=box.DOUBLE
        ))
        
        while True:
            self.display_menu()
            choice = Prompt.ask(
                "[bold cyan]Please enter your choice[/bold cyan] [dim](0-6)[/dim]",  # CHANGE TO 0-6
                choices=["0", "1", "2", "3", "4", "5", "6"],  # ADD "6"
                show_choices=False
            )
            
            action = self.menu_actions.get(choice, self.invalid_choice)
            result = action()
            
            if result is False:
                break

# ==================== Entry Point ====================
if __name__ == "__main__":
    try:
        app = DailyBugleMenu()
        app.run()
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("\nPlease set your NY Times API key:")
        print("export NYTIMES_API_KEY='your-api-key-here'")

