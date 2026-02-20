## Plan: Daily NY Times News Scraper (Daily Bugle)

A Python script that fetches morning news from the New York Times API at 8:00am daily, formats it, and displays it in the terminal. Uses scheduling automation, API integration, and JSON parsing

First Step: Get NYT API keys for env variables, get error handling for the API failures, and examine the data that the API returns for formatting later
Second Step: Create the actual news fetching function, parse JSON response, extract what I want, and format it into a readable display
Third Step: Add the scheduling mechanism to trigger the fetch function daily at 8:00am with a while True loop that checks the schedule and sleeps between checks
Fourth Step: Build a CLI menu system with options to: fetch news now, view/change schedule time, run scheduler, save news to JSON file, exit
Fifth Step: Implement data persistence to save fetched articles to an archive with timestamps to allow users to review past fetches

## Consider:

API Choice: Top Stories vs. Article Search
Scheduler deployment: schedule library vs system cron job (probably more useful to go with the latter since that will give me more optionality when picking the time)
Display formatting: plain text output vs rich formatting with rich library (plain text formatting early on and then convert to rich after core functionality is stable)

## Consulted Copilot for highest efficiency build for my requirements:

Create main DailyBugle class in [daily-bugle.py](Day 7/The Daily Bugle/daily-bugle.py) with __init__ to initialize NYTimesAPI, NewsArchive, and NewsScheduler instances as attributes (composition pattern like User containing Inbox)

Implement handler methods for each menu option: view_todays_stories(), manage_schedule(), toggle_scheduler(), archive_news(), view_old_archives() - each method encapsulates one menu choice's logic

Build dictionary dispatch system mapping choice strings to methods: self.menu_actions = {'1': self.view_todays_stories, '2': self.manage_schedule, ...} - stores function references without calling them

Create run() method with while True loop that displays menu, gets input, and executes with self.menu_actions.get(choice, self.invalid_choice)() - automatically calls correct method or default handler

Add helper methods display_menu() for printing options and invalid_choice() for handling bad input, keeping run() clean and focused

## Further Considerations
Error handling: Wrap menu_actions.get(choice)() in try-except to catch errors within handler methods? Prevents crashes and allows graceful error messages per your error handling experience? (I would rather be able to catch the errors earlier on in the code than the dispatch level of the menu actions, instead I will raise errors within the handlers and use try/except in the handlers and then use a safety net on the dispatch level to catch anything extrenuous)

Menu extensibility: Consider adding a 7th option "Settings" now, or design so new options only require: add method + add to dispatch dict? Dictionary dispatch makes adding features trivial vs expanding if-elif chains?

Input validation: Pre-validate choice before dispatch (check if in valid range), or let dict.get(choice, default) handle it? Second approach is more Pythonic and efficient?

## Future Features?
Implement Times Newswire API for NYT to get links and metadata for Times' articles as soon as they are published on NYTimes.com. The Times Newswire API provides an up-to-the-minute stream of published articles. 
    
### News Aggregation System - The Daily Bugle

#### Core Architecture
- **Abstract Base Class Pattern** (`NewsAPI`):
  - Defined common interface for all news sources
  - Abstract methods: `fetch_top_stories()`, `search_articles()`, `get_available_sections()`
  - Shared rate limiter across all API instances
  - Enforced consistent API design with `@abstractmethod`

- **Multiple API Integrations**:
  - **NY Times API** (`NYTimesAPI`): Top Stories and Article Search endpoints
  - **The Guardian API** (`GuardianAPI`): UK news with section browsing
  - **NewsAPI.org** (`NewsAPIOrg`): Multi-source news aggregator
  - **GNews API** (`GNewsAPI`): Alternative news source with topic filtering
  - **Mediastack API** (`MediastackAPI`): International news coverage
  - **Currents API** (`CurrentsAPI`): Latest news with category support

#### Rate Limiting & Persistence
- **RateLimiter Class**:
  - Tracks API calls per source with timestamps
  - Rolling time windows (per minute, hour, day, month)
  - Prevents quota exhaustion with proactive checks
  - Shared rate limiter pattern across all API instances
  - **State Persistence**: 
    - Saves call history to `~/.dailybugle/rate_limit_state.json`
    - Loads previous session's usage on startup
    - Auto-cleanup of expired call timestamps
    - Persists across application restarts

- **Rate Limit Features**:
  - Pre-request validation with `_check_rate_limit()`
  - Time-until-reset calculations
  - Human-readable wait time messages (hours/minutes/seconds)
  - API status dashboard showing all sources
  - Color-coded warnings (green/yellow/red based on remaining calls)

#### Configuration Management
- **Persistent User Preferences** (`~/.dailybugle/config.json`):
  - Saves selected API source between sessions
  - Loads last-used API on startup
  - Falls back to default if preference unavailable
  - Timestamps for config tracking

#### Rich Terminal UI
- **Enhanced Visual Design** with Rich library:
  - **Styled Tables**: Bordered tables with color-coded columns
  - **Panels**: Boxed sections with custom borders (ROUNDED, DOUBLE)
  - **Progress Indicators**: Loading spinners during API requests
  - **Color Coding**: Cyan headers, yellow titles, green success, red errors
  - **Interactive Prompts**: Rich's `Prompt.ask()` and `Confirm.ask()`
  - **Status Information**: Real-time rate limit display in menu

- **Menu System**:
  - Color-coded menu options with emojis
  - Current API and rate limit status always visible
  - Formatted article lists with overflow handling
  - Styled article details in panels
  - Archive management with timestamps

#### Article Management
- **Article Class**:
  - Structured data: title, abstract, byline, url, published_date, section, source
  - Rich-formatted display with panels and styled text
  - Timestamp tracking with `fetched_at`
  - Dictionary serialization for JSON storage

- **Archive System** (`NewsArchive`):
  - In-memory article storage during session
  - View archived articles with formatted table
  - Open articles in default browser
  - Archive counter in menu

#### Scheduled Automation
- **Automated News Fetching** (`scheduled-fetch.py`):
  - Imports classes from main application (modular design)
  - Reads user's preferred API from config
  - Falls back to multiple sources if no preference
  - Saves articles to `~/.dailybugle/archive/scheduled_articles.json`
  - Logs fetch operations to `fetch_log.txt`
  - Designed for cron job execution

- **Morning Brief** (`morning-brief.py`):
  - Reads cached articles from scheduled fetch
  - Displays top 5 recent articles
  - Time-gated display (7-10 AM via `.zshrc`)
  - Quick headlines before full app launch

- **Shell Scripts**:
  - `~/bin/dailybugle`: Main app launcher with venv activation
  - `~/bin/dailybugle-fetch`: Scheduled fetch wrapper for cron
  - `~/bin/dailybugle-brief`: Morning headlines display
  - All scripts handle virtual environment activation

#### Cron Job Setup
- **Automated Scheduling**:
  - Cron job fetches news at 6:30 AM daily
  - Terminal shows brief automatically on morning launch
  - Persistent rate limits prevent quota issues across scheduled runs
  - Logs for debugging scheduled operations

### Key Concepts Learned

#### Design Patterns
- **Abstract Base Classes**: Enforcing consistent interfaces across implementations
- **Shared State Pattern**: Single rate limiter instance for all APIs
- **Factory Pattern**: Dynamic API registration and selection
- **Separation of Concerns**: API logic, UI, persistence all separated

#### API Integration
- **REST API Consumption**: Making HTTP requests with `requests` library
- **Error Handling**: Graceful degradation when APIs fail
- **Rate Limiting**: Respecting API quotas and usage windows
- **Pagination**: Fetching multiple pages of results
- **API Key Management**: Environment variables with `python-dotenv`

#### Data Persistence
- **JSON Storage**: Serializing Python objects to JSON
- **File System Operations**: Creating directories with `Path.mkdir()`
- **State Management**: Loading and saving application state
- **Session Continuity**: Maintaining state across restarts

#### Terminal UI Best Practices
- **Rich Library**: Professional terminal formatting
- **Progress Feedback**: Loading indicators for long operations
- **Color Psychology**: Green for success, red for errors, yellow for warnings
- **Table Design**: Organizing data in readable columns
- **Interactive Prompts**: Validating user input with choices

#### System Integration
- **Virtual Environments**: Activating venv in shell scripts
- **Shell Scripting**: Bash wrappers for Python applications
- **PATH Management**: Adding custom commands to shell
- **Cron Jobs**: Scheduling automated tasks
- **Zsh Configuration**: Customizing shell behavior

#### Error Handling Strategies
- **API Failures**: Try-except blocks with informative messages
- **Rate Limit Errors**: Calculating and displaying wait times
- **File I/O Errors**: Handling missing or corrupted config files
- **Input Validation**: Checking user input before processing

### Project Structure
Day 7/
├── The Daily Bugle/
│ ├── daily_bugle.py # Main application
│ ├── scheduled-fetch.py # Automated fetching
│ ├── morning-brief.py # Quick headlines
│ └── .env # API keys (not in git)
├── ~/bin/
│ ├── dailybugle # Main launcher
│ ├── dailybugle-fetch # Fetch wrapper
│ └── dailybugle-brief # Brief display
└── ~/.dailybugle/
├── config.json # User preferences
├── rate_limit_state.json # Rate limit history
├── cron.log # Cron execution log
└── archive/
├── scheduled_articles.json
└── fetch_log.txt

### Technical Achievements
- ✅ Abstract base class with multiple concrete implementations
- ✅ Persistent rate limiting across sessions
- ✅ Rich terminal UI with tables, panels, and colors
- ✅ Configuration management with JSON
- ✅ Scheduled automation with cron
- ✅ Shell script integration with virtual environments
- ✅ Multi-source news aggregation
- ✅ Interactive pagination for large result sets
- ✅ Browser integration for opening articles
- ✅ Modular code organization with imports

### Real-World Applications
- **API Consumption**: Working with external data sources
- **Rate Limit Management**: Respecting service quotas
- **User Preferences**: Saving and loading configuration
- **Automation**: Scheduled tasks without manual intervention
- **Terminal UX**: Creating professional CLI applications
- **Error Recovery**: Graceful handling of failures
- **State Persistence**: Maintaining context across sessions