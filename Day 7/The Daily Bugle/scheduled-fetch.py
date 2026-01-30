#!/usr/bin/env python3
"""
Scheduled news fetcher that runs automatically via cron
Fetches top stories and saves them to archive without user interaction
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

# Add the Daily Bugle directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

# Import from your main daily-bugle.py file
from daily_bugle import (
    NYTimesAPI,
    GuardianAPI,
    NewsAPIOrg,
    GNewsAPI,
    MediastackAPI,
    CurrentsAPI,
    Article
)

class ScheduledNewsArchive:
    """Archive specifically for scheduled fetches - saves to JSON"""
    
    def __init__(self):
        self.archive_dir = Path.home() / ".dailybugle" / "archive"
        self.archive_dir.mkdir(parents=True, exist_ok=True)
        self.archive_file = self.archive_dir / "scheduled_articles.json"
        self.log_file = self.archive_dir / "fetch_log.txt"
        self.articles = []
        self._load_archive()
    
    def _load_archive(self):
        """Load existing archived articles from JSON"""
        if self.archive_file.exists():
            try:
                with open(self.archive_file, 'r') as f:
                    data = json.load(f)
                    self.articles = data
            except json.JSONDecodeError:
                self.articles = []
    
    def _save_archive(self):
        """Save articles to JSON file"""
        with open(self.archive_file, 'w') as f:
            json.dump(self.articles, f, indent=2)
    
    def add_article(self, article):
        """Add article to archive (avoid duplicates by URL)"""
        if not any(a['url'] == article.url for a in self.articles):
            article_dict = {
                'title': article.title,
                'abstract': article.abstract,
                'byline': article.byline,
                'url': article.url,
                'published_date': article.published_date,
                'section': article.section,
                'source': article.source,
                'fetched_at': datetime.now().isoformat()
            }
            self.articles.append(article_dict)
            return True
        return False
    
    def log_fetch(self, message):
        """Log fetch operations"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")

def load_user_config():
    """Load the user's saved API preference"""
    config_file = Path.home() / ".dailybugle" / "config.json"
    
    if config_file.exists():
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                return config.get('current_api')
        except (json.JSONDecodeError, IOError):
            pass
    
    return None

def fetch_news_scheduled():
    """Main function to fetch news on schedule"""
    archive = ScheduledNewsArchive()
    new_articles_count = 0
    
    # Load user's preferred API
    preferred_api = load_user_config()
    
    # Map API keys to classes and default sections
    api_map = {
        'nytimes': (NYTimesAPI, 'home'),
        'guardian': (GuardianAPI, 'world'),
        'newsapi': (NewsAPIOrg, 'general'),
        'gnews': (GNewsAPI, 'general'),
        'mediastack': (MediastackAPI, 'general'),
        'currents': (CurrentsAPI, 'news'),
    }
    
    # If user has a preference, use only that API; otherwise fetch from multiple
    if preferred_api and preferred_api in api_map:
        apis_to_fetch = [(preferred_api, *api_map[preferred_api])]
        archive.log_fetch(f"Using user's preferred API: {preferred_api}")
    else:
        # Fallback: fetch from multiple sources
        apis_to_fetch = [
            ('nytimes', NYTimesAPI, 'home'),
            ('guardian', GuardianAPI, 'world'),
        ]
        archive.log_fetch("No user preference found, using default sources")
    
    archive.log_fetch("=== Starting scheduled fetch ===")
    
    for api_key, api_class, section in apis_to_fetch:
        try:
            api = api_class()
            archive.log_fetch(f"Fetching from {api.get_api_name()} - {section}")
            
            articles = api.fetch_top_stories(section=section)
            
            for article in articles[:10]:  # Fetch top 10 from each source
                if archive.add_article(article):
                    new_articles_count += 1
            
            archive.log_fetch(f"✓ Successfully fetched from {api.get_api_name()}")
            
        except Exception as e:
            archive.log_fetch(f"✗ Error fetching from {api_key}: {e}")
    
    # Save archive
    archive._save_archive()
    archive.log_fetch(f"=== Fetch complete: {new_articles_count} new articles archived ===\n")
    
    return new_articles_count

if __name__ == "__main__":
    try:
        count = fetch_news_scheduled()
        print(f"Scheduled fetch complete: {count} new articles archived")
    except Exception as e:
        print(f"Error during scheduled fetch: {e}")
        sys.exit(1)