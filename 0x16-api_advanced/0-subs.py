#!/usr/bin/python3
"""
queries the Reddit API and returns the number of total subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'canBeAnything'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        return res['data']['subscribers']
    else:
        return 0
