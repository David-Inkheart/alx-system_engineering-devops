#!/usr/bin/python3
"""
queries the Reddit API and returns the number of total subscribers for a given
subreddit. If an invalid subreddit is given, the function should return 0.
"""
import requests
import sys


def top_ten(subreddit):
    """returns the number of subscribers"""
    listing = 'hot'  # controversial, best, hot, new, random, rising, top
    base_url = 'https://www.reddit.com/r/{}/{}.json'.format(subreddit, listing)
    headers = {'User-agent': 'canBeAnything'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        post_titles = []
        for i, post in enumerate(res['data']['children']):
            if i >= 10:
                break
            titles = post['data']['title']
            post_titles.append(titles)
        p_t = post_titles
        for item in p_t:
            print(item)
    else:
        print('None')
