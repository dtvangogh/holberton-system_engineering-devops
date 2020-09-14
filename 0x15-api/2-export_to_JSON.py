#!/usr/bin/python3
"""
export data to json
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """
    Records all tasks that are owned by this employee
    """
    userId = int(argv[1])
    user_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId)).json().get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos?userId={}".format(userId)).json()
    task_data = []
    json_object = {}
    for task in tasks:
        task_dictionary = {}
        task_dictionary["task"] = task.get('title')
        task_dictionary["completed"] = task.get("completed")
        task_dictionary["username"] = user_name
        task_data.append(task_dictionary)
    json_object[userId] = task_data
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(json_object, jsonfile)
