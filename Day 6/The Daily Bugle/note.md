Plan: Daily NY Times News Scraper (Daily Bugle)

A Python script that fetches morning news from the New York Times API at 8:00am daily, formats it, and displays it in the terminal. Uses scheduling automation, API integration, and JSON parsing

First Step: Get NYT API keys for env variables, get error handling for the API failures
Second Step: Create the actual news fetching function, parse JSON response, extract what I want, and format it into a readable display
Third Step: Add the scheduling mechanism to trigger the fetch function daily at 8:00am with a while True loop that checks the schedule and sleeps between checks
Fourth Step: Build a CLI menu system with options to: fetch news now, view/change schedule time, run scheduler, save news to JSON file, exit
Fifth Step: Implement data persistence to save fetched articles to an archive with timestamps to allow users to review past fetches

Consider:
API Choice: Top Stories vs. Article Search
Scheduler deployment: schedule library vs system cron job (probably more useful to go with the latter)
Display formatting: plain text output vs rich formatting with rich library