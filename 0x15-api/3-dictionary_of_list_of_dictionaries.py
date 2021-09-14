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
        user_iid = pos.get("id")
        dic[user_iid] = []
        usr_dic[user_iid] = pos.get("username")
    alls = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for taskss in alls:
        taskss = {}
        user_iid = taskss.get("userId")
        taskss["task"] = taskss.get('title')
        taskss["completed"] = taskss.get('completed')
        taskss["username"] = usr_dic.get(user_iid)
        dic[str(user_iid)].append(taskss)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(dic, jsonfile)
