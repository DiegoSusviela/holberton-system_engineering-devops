#!/usr/bin/python3
""" Reddit API"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r_u = requests.get('https://www.reddit.com/r/' +
                       subreddit + '/about.json',
                       headers=headers, allow_redirects=False)
    if r_u.status_code == 200:
        usr = r_u.json().get('data')
        return usr.get('subscribers')
    return 0
