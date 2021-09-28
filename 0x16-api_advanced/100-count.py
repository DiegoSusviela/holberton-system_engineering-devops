#!/usr/bin/python3
""" Reddit API"""
import requests


def count_words(subreddit, word_list, pagination="", results={}, count=0):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/' + subreddit +\
          '/hot.json?after={}'.format(pagination)
    r_u = requests.get(url, headers=headers, allow_redirects=False)
    if r_u.status_code != 200:
        return None
    res = r_u.json()
    hot = res.get('data').get('children')
    for pos in hot:
        tit = pos.get('data').get('title')
        for pos2 in word_list:
            for pos3 in tit.split():
                if pos2.lower() in pos3.lower():
                    count += 1
            results[pos2] = count
        count = 0
    pagination = res.get('data').get('after')
    if pagination is not None:
        count_words(subreddit, word_list, pagination, results, count)
    else:
        for key, value in results.items():
            print("{}: {}".format(key, value))
