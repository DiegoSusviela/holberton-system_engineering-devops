#!/usr/bin/python3
""" Reddit API"""
import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r_u = requests.get('https://www.reddit.com/r/' +
                       subreddit + '/hot.json?limit=10',
                       headers=headers, allow_redirects=False)
    if r_u.status_code < 300:
        json = r_u.json()
        data_dict = json.get('data')
        hot = data_dict.get('children')
        for pos in hot:
            dat_dic = pos.get('data')
            print(dat_dic.get('title'))
    else:
        print(None)
