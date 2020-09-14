#!/usr/bin/python3
"""
fetches from https://jsonplaceholder.typicode.com and pushes
information about the employee todo list. takes userId of employee as argument
"""

import requests
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo_list = requests.get("https://jsonplaceholder.typicode.com/
                             todos?userId={}".format(userId),
                             verify=False).json()
    number_of_done_tasks = []
    for task in todo_list:
        if task.get('completed') is True:
            number_of_done_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(number_of_done_tasks), len(todo_list)))
    separator = "\n"
    print(separator.join("\t {}".format(task)
          for task in number_of_done_tasks))
