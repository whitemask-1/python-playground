#!/usr/bin/env python3
"""Morning Brief - Quick news summary from cache"""

import json
from pathlib import Path

def show_morning_brief():
    archive_file = Path.home() / ".dailybugle" / "archive" / "scheduled_articles.json"
    
    if not archive_file.exists():
        print("\n📰 Daily Bugle: No cached news. Run 'dailybugle-fetch' first.\n")
        return
    
    try:
        with open(archive_file, 'r') as f:
            articles = json.load(f)
        
        if not articles:
            return
        
        recent = sorted(articles, key=lambda x: x.get('fetched_at', ''), reverse=True)[:5]
        
        print("\n" + "="*70)
        print("📰 DAILY BUGLE - MORNING BRIEF")
        print(f"   {len(articles)} articles | Updated: {recent[0].get('fetched_at', '')[:10]}")
        print("="*70 + "\n")
        
        for i, article in enumerate(recent, 1):
            print(f"{i}. {article['title']}")
            print(f"   {article['source']} | {article['section']}")
            print(f"   {article['abstract'][:80]}...")
            print()
        
        print("="*70)
        print("Type 'dailybugle' for full interactive reader")
        print("="*70 + "\n")
        
    except Exception as e:
        print(f"\n📰 Error: {e}\n")

if __name__ == "__main__":
    show_morning_brief()