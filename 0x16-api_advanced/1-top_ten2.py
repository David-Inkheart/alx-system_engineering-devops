#!/usr/bin/python3
"""
queries the Reddit API and returns the number of total subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests
import sys


def top_ten(subreddit):
    """returns the number of subscribers"""
    limit = 10  # default = 25, max = 100
    listing = 'hot'  # controversial, best, hot, new, random, rising, top
    base_url = 'https://www.reddit.com/r/{}/{}.json?limit={}'.format(subreddit, listing, limit)
    headers = {'User-agent': 'canBeAnything'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        post_titles = []
        for post in res['data']['children']:
            titles = post['data']['title']
            post_titles.append(titles)
        for k in post_titles:
            print(k)
    else:
        return None
