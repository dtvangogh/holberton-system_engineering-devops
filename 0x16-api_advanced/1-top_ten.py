#!/usr/bin/python3
"""This module queries reddit api"""
import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts listed
    for subreddit passed as argv[2]
    """
    user_agent = {'User-agent': 'dtvangogh'}
    req = requests.get(
        "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit),
        headers=user_agent, allow_redirects=False)
    data = req.json().get('data')
    if data is None:
        print(None)
    else:
        children = data.get('children')
        for child in children:
            print(child.get('data').get('title'))
