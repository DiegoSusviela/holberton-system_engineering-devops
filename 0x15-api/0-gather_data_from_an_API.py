#!/usr/bin/python3
""" a wopa"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                     format(userId), verify=False).json()
    all = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                       format(userId), verify=False).json()
    completed_tasks = []
    for task in all:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(r.get('name'), len(completed_tasks), len(all)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))
