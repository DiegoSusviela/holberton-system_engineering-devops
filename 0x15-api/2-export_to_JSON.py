#!/usr/bin/python3
""" a wopa"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{:}'
                     .format(argv[1])).json()
    all = requests.get(
        'https://jsonplaceholder.typicode.com/todos/?userId={:}'
        .format(argv[1])).json()
    user_id = argv[1]
    usr = r.get('username')
    tsd = {}
    task_list = []
    for item in all:
        task = {}
        task["task"] = item.get('title')
        task["completed"] = item.get('completed')
        task["username"] = usr
        task_list.append(task)
    tsd[user_id] = task_list
    with open("{:}.json".format(user_id), 'w') as f:
        json.dump(tsd, f)
