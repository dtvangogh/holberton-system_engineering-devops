#!/usr/bin/python3
"""
fetches from https://jsonplaceholder.typicode.com and pushes  information about the employee todo list. takes userId of employee as argument
"""

import requests
from sys import argv
import csv

if __name__ == '__main__':
    userId = int(argv[1])
    user_name = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId)).json().get("username")
    tasks = requests.get("https://jsonplaceholder.typicode.com/"
                             "todos?userId={}".format(userId)).json()
    with open("{}.csv".format(userId), "w") as cvsfile:
        write = csv.writer(cvsfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            write.writerow([userId, user_name,
                           task.get("completed"), task.get("title")])
