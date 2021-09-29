#!/usr/bin/python3
""" Reddit API"""
import requests


def count_words(subreddit, word_list, pagination="", results={}, count=0):
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get('https://www.reddit.com/r/{:}/hot.json?after={:}'.format(
        subreddit, after), headers=headers, allow_redirects=False)
    if r.status_code == 200:
        json = r.json()
        daddy = json.get('data')
        polly = daddy.get('children')
        for pos in polly:
            podi = pos.get('data')
            for word in word_list:
                tt = podi.get('title').split()
                tc = []
                for j in tt:
                    tc.append(j.upper())
                count = tc.count(word.upper())
                if word_dict.get(word):
                    word_dict[word] += count
                else:
                    word_dict[word] = count
        after = daddy.get('after')
        if daddy.get('after') is None:
            sorted_list = sorted(word_dict.items(), key=operator.itemgetter(1),
                                 reverse=True)
            for i in range(len(sorted_list) - 1):
                if sorted_list[i][1] == sorted_list[i+1][1]:
                    if sorted_list[i][0] > sorted_list[i+1][0]:
                        sorted_list[i], sorted_list[i+1] = sorted_list[
                            i+1], sorted_list[i]
            for item in sorted_list:
                if item[1] > 0:
                    print("{:}: {:}".format(item[0], item[1]))
            return
        return count_words(subreddit, word_list, word_dict, after)
    else:
        return
