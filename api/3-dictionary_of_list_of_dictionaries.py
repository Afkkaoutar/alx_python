#!/usr/bin/python
import requests
import json


def export_todo_data():
    # Retrieve employee details
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    employees = response.json()

    todo_data = {}
    for employee in employees:
        employee_id = employee["id"]
        employee_name = employee["name"]

        # Retrieve TODO list for the employee
        url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response = requests.get(url)
        todos = response.json()

        # Prepare TODO list data for the employee
        employee_tasks = []
        for todo in todos:
            task_data = {
                "username": employee_name,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            employee_tasks.append(task_data)

        # Add employee's TODO list data to the main dictionary
        todo_data[str(employee_id)] = employee_tasks

    # Export TODO list data to JSON file
    filename = "todo_all_employees.json"