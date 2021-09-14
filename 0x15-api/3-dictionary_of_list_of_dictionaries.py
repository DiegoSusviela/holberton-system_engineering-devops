#!/usr/bin/python3
""" a wopa"""

import json
import requests

if __name__ == '__main__':
    r = requests.get("https://jsonplaceholder.typicode.com/users",
                     verify=False).json()
    dico = {}
    usr_dic = {}
    for pos in r:
        user_iid = pos.get("id")
        dico[user_iid] = []
        usr_dic[user_iid] = pos.get("username")
    alls = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in alls:
        taskss = {}
        user_iid = task.get("userId")
        taskss["task"] = task.get('title')
        taskss["completed"] = task.get('completed')
        taskss["username"] = usr_dic.get(user_iid)
        dico[str(user_iid)].append(taskss)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dico, jsonfile)
