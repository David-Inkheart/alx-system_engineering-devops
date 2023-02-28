#!/usr/bin/python3

"""
queries the Reddit API and returns the titles of a given subreddit.
If an invalid subreddit is given, the function should return None. and
prints a sorted count of given keywords (case-insensitive, delimited by spaces
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function returns None.
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    headers = {'User-Agent': 'something'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()['data']
        for post in data['children']:
            hot_list.append(post['data']['title'])
        if data['after'] is not None:
            recurse(subreddit, hot_list, after=data['after'])
        return hot_list
    else:
        return None


def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API for the hot articles of a given
    subreddit, counts the occurrences of each word in the provided list,
    and prints the results.
    """
    hot_list = recurse(subreddit)
    if hot_list is None:
        return None
    word_counts = {}
    for word in word_list:
        word_counts[word.lower()] = 0
    for title in hot_list:
        for word in word_list:
            count = title.lower().count(word.lower())
            if count > 0:
                word_counts[word.lower()] += count
    results = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    for word, count in results:
        if count > 0:
            print("{}: {}".format(word, count))
