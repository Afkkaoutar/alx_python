#!/usr/bin/python3
"""Gather Data from API.

This script uses REST API (with employee data)
and returns info about the employee's TODO list progress.

The extension to CSV format is added"""
import csv
import requests
import sys

# function fetches employee details & calculates completed tasks
def generate_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # fetches employee's name & other details
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

    # returns the TODO list progress
    return employee_name, completed_count, total_tasks, completed_tasks

# function block prints the TODO list in the specified format
def print_todo_list_progress(employee_name, completed_count, total_tasks, completed_tasks):
    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

# this new function block exports the data to a CSV file
def export_to_csv(employee_id, employee_name, completed_tasks):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for task in completed_tasks:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

# # checks if the script is being run directly
# if that's the case, it then takes the employee data as a command-line argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_count, total_tasks, completed_tasks = generate_employee_todo_progress(employee_id)
    print_todo_list_progress(employee_name, completed_count, total_tasks, completed_tasks)

    # exports to CSV
    export_to_csv(employee_id, employee_name, completed_tasks)

    # this block reads the CSV file
    def user_info(employee_id):
        filename = f"{employee_id}.csv"
        with open(f"{employee_id}.csv", 'r') as f:
            pass