#!/usr/bin/python3
""" a wopa"""

import requests
import csv
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(userId), verify=False).json()
    all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                       format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        tsd = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in all:
            tsd.writerow([int(userId), r.get('username'),
                          task.get('completed'),
                          task.get('title')])
