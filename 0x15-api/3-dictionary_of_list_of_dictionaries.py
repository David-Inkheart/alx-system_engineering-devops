#!/usr/bin/python3
"""
Extend the python script from exercise 0 to export data in JSON format.
File name must be: todo_all_employees.json
"""
import json
import requests


if __name__ == "__main__":
    users = requests.get("http://jsonplaceholder.typicode.com/users").json()
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos").json()
    data_load = {}

    for user in users:
        employee_id = user.get("id")
        username = user.get("username")
        all_tasks = []

        for task in tasks:
            if (task.get("userId") == employee_id and task.get("completed")):
                temp_task = {}
                temp_task["task"] = task.get("title")
                temp_task["completed"] = task.get("completed")
                temp_task["username"] = username
                all_tasks.append(temp_task)

        data_load[employee_id] = all_tasks

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(data_load, jsonfile)
