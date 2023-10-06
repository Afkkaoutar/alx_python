#!/usr/bin/python3
"""Gather Data from API.

This script uses REST API (with employee data)
and returns info about the employee's TODO list progress."""

import requests
import sys

# this function block gets employee's TODO progress
def generate_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # fetches employee's name and other details
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data['name']

    # fetches the employee's TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # calculates the employee's completed tasks
    completed_tasks = [todo for todo in todos_data if todo['completed']]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # displays the TODO list progress in this format
    return employee_name, completed_count, total_tasks, completed_tasks

# this function prints the TODO list that has been generated in the format below
def print_todo_list_progress(employee_name, completed_count, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

# this block checks if the script is being run directly
# and takes the employee ID as a command line argument if that's the case
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_count, total_tasks, completed_tasks = generate_employee_todo_progress(employee_id)
    print_todo_list_progress(employee_name, completed_count, total_tasks, completed_tasks)