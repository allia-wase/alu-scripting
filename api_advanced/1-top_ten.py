#!/usr/bin/python3
"""
Queries Reddit API & prints titles of first 10 hot posts for a subreddit.
Returns 'OK' if subreddit doesn't exist.
"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "CustomUserAgent"}
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            data = res.json().get("data", {}).get("children", [])
            for post in data:
                print(post["data"]["title"])
        elif res.status_code == 404:
            print("OK")
        else:
            print("OK")
    except Exception:
        print("OK")

if __name__ == "__main__":
    top_ten("programming")  # Test with existing subreddit
    top_ten("nonexistent123")  # Test with non-existent subreddit
