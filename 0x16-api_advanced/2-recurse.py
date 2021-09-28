#!/usr/bin/python3
""" Reddit API"""
import requests


def recurse(subreddit, hot_list=[], pagination=""):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r_u = requests.get('https://www.reddit.com/r/' + subreddit +\
          	           '/hot.json?after={}'.format(pagination)' +
                       subreddit + '/hot.json?limit=10',
                       headers=headers, allow_redirects=False)
    if r_u.status_code != 200:
        return None
    res = r_u.json()
    hot = res.get('data').get('children')
    for pos in hot:
        hot_list.append(pos.get('data').get('title'))
    pagination = res.get('data').get('after')
    if pagination is not None:
        recurse(subreddit, hot_list, pagination)
    return hot_list
