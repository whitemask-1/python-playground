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
Display formatting: plain text output vs rich formatting with rich library (plain text formatting early oj and then convert to rich after core functionality is stable)

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
    