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
    emp = requests.get("https://jsonplaceholder.typicode.com/users").json()
    json_data = {}
    for employee in emp:
        employee_data = []
        userId = employee['id']
        tasks = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos?userId={}".format(userId)).json()
        for task in tasks:
            task_data = {}
            task_data["task"] = task.get('title')
            task_data["completed"] = task.get("completed")
            task_data["username"] = employee['username']
            employee_data.append(task_data)
        json_data[userId] = employee_data
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(json_data, jsonfile)
