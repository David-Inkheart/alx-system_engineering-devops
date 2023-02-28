#!/usr/bin/python3
"""
sample code to list all elements I can extract under
a reddit API subreddit listing
"""
import requests
import sys


def list_of_elements(subreddit):
    """returns a list of elements to extract"""
    base_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-agent': 'anything'}
    response = requests.get(base_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        res = response.json()
        return res['data']
    else:
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        elements = list_of_elements(sys.argv[1]).keys()
        for k in elements:
            print(k)
