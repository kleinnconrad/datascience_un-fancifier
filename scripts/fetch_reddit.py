import feedparser
from bs4 import BeautifulSoup
import os

# Reddit often blocks default Python user agents. 
# Setting a custom User-Agent prevents HTTP 429 (Too Many Requests) errors.
feedparser.USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"

# The base URL without tracking parameters
POST_URL = "https://www.reddit.com/r/dataengineering/comments/1se66gi/unfancify_data_science/"
RSS_URL = POST_URL + ".rss"

def fetch_and_parse():
    print(f"Fetching RSS feed from: {RSS_URL}")
    feed = feedparser.parse(RSS_URL)
    
    # Ensure the target directory exists
    os.makedirs("reddit", exist_ok=True)
    
    with open("reddit/reddit_feedback.md", "w", encoding="utf-8") as f:
        f.write("# Reddit Feedback: Unfancify Data Science\n\n")
        f.write(f"**Source:** [Reddit Post]({POST_URL})\n\n")
        f.write("---\n\n")
        
        if not feed.entries:
            f.write("*No comments found or unable to fetch feed.*\n")
            print("No entries found in the RSS feed.")
            return

        for i, entry in enumerate(feed.entries):
            author = entry.author if hasattr(entry, 'author') else 'Unknown Author'
            
            # Reddit RSS feeds contain HTML formatting in the summary. 
            # BeautifulSoup extracts clean, readable text.
            soup = BeautifulSoup(entry.summary, "html.parser")
            text = soup.get_text(separator="\n", strip=True)
            
            # The first entry in a Reddit post RSS feed is always the original post
            if i == 0:
                f.write(f"## Original Post by {author}\n\n")
            else:
                f.write(f"### Comment by {author}\n\n")
                
            f.write(f"{text}\n\n")
            f.write("---\n\n")
            
    print("Successfully updated reddit/reddit_feedback.md")

if __name__ == "__main__":
    fetch_and_parse()
  
