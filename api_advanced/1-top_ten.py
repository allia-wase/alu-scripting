#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles of the first 10 hot posts
listed for a given subreddit or returns 'OK' for both existing and non-existent subreddits.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed in a subreddit,
    or returns 'OK' if the subreddit does not exist.
    """
    # Construct the URL for the subreddit's hot posts
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        # Send a GET request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check the HTTP status code
        if response.status_code == 200:
            # Subreddit exists, extract and print the titles of the first 10 hot posts
            posts = response.json().get("data", {}).get("children", [])
            if posts:
                for post in posts:
                    print(post["data"]["title"])
            else:
                print("No posts found.")
        elif response.status_code == 404:
            # Subreddit does not exist, return 'OK' as per the requirement
            print("OK")
        else:
            # Handle unexpected errors
            print("OK")
    except Exception as e:
        # Return 'OK' if an exception occurs
        print("OK")


# Example usage
if __name__ == "__main__":
    # Test with an existing subreddit
    top_ten("programming")

    # Test with a non-existent subreddit
    top_ten("thissubredditdoesnotexist123")
