#!/usr/bin/python3
"""This module uses the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for subreddit as argv[2]"""
    user_agent = {'User-agent': 'dtvan'}
    req = requests.get(
        "https://www.reddit.com/r/{}/about/.json".format(subreddit),
        headers=user_agent, allow_redirects=False)
    data = req.json().get('data')
    if data is None:
        return 0
    subscribers = data.get('subscribers')
    return subscribers
