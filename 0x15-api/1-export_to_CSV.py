#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""

import requests
import sys
import csv


def todo_list_progress(employee_id):
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    employee_data = requests.get(url).json()
    employee_name = employee_data['name']

    url = "https://jsonplaceholder.typicode.com/todos?userId={}"\
        .format(employee_id)
    todos = requests.get(url).json()

    done_tasks = [(str(employee_id), employee_name, str(task['completed']),
                   task['title']) for task in todos]

    file_name = "{}.csv".format(employee_id)
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["USER_ID", "USERNAME",
                        "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(done_tasks)

    print("Data exported successfully to file: {}".format(file_name))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 todo_list_progress.py [employee_id]")
    else:
        employee_id = int(sys.argv[1])
        todo_list_progress(employee_id)
