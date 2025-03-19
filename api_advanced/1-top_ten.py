#!/usr/bin/python3
""" top_ten.py """
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed in a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "my_bot/1.0"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit exists and API response is valid
    if response.status_code != 200:
        print(None)
        return

    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        for post in posts:
            print(post["data"]["title"])
    except Exception:
        print(None)
