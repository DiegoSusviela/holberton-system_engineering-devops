#!/usr/bin/python3
""" a wopa"""

import json
import requests

if __name__ == '__main__':
    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     verify=False).json()
    dic = {}
    usr_dic = {}
    for pos in r:
        user_id = pos.get("id")
        dic[user_id] = []
        usr_dic[user_id] = pos.get("username")
    all = requests.get("https://jsonplaceholder.typicode.com/todos",
                       verify=False).json()
    for task in all:
        task = {}
        user_id = task.get("userId")
        task["task"] = task.get('title')
        task["completed"] = task.get('completed')
        task["username"] = usr_dic.get(user_id)
        dic.get(user_id).append(task)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dic, jsonfile)
