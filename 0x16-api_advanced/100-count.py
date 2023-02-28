#!/usr/bin/python3
"""
queries the Reddit API and returns the titles of a given subreddit.
If an invalid subreddit is given, the function should return None. and
prints a sorted count of given keywords (case-insensitive, delimited by spaces
"""

import requests
import sys


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}
    if after is None:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                     after)

    headers = {
        "User-Agent": "newcode"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return

    data = response.json().get("data")
    after = data.get("after")
    children = data.get("children")

    for child in children:
        title = child.get("data").get("title").lower()
        for word in word_list:
            word = word.lower()
            if word in counts:
                counts[word] += title.count(word)
            else:
                counts[word] = title.count(word)

    if after is None:
        counts = {word: count for word, count in counts.items() if count > 0}
        for key, value in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            print("{}: {}".format(key, value))
        return
    else:
        return count_words(subreddit, word_list, after, counts)
