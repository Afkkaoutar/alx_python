#!/usr/bin/python
"""
import requests module
"""
import requests
""" import sys"""
import sys
""" import json"""
import json

"""
Get the employee ID from the command line arguments
"""
employee_id = sys.argv[1]

""" 
Define the base URL for the API
"""
base_url = "https://jsonplaceholder.typicode.com/users/"

""" Get the employee details from the API"""
employee = requests.get(base_url + employee_id).json()

""" Get the employee name"""
employee_name = employee["name"]

""" Get the employee TODO list from the API"""
todos = requests.get(base_url + employee_id + "/todos").json()

""" Initialize the total and done tasks counters"""
total_tasks = 0
done_tasks = 0

""" Initialize a list for tasks"""
tasks_list = []

"""
 Loop through the todos list and update the counters and tasks list
 """
for todo in todos:
    total_tasks += 1
    task_data = {
        "task": todo["title"],
        "completed": todo["completed"],
        "username": employee["username"]
    }
    tasks_list.append(task_data)
    if todo["completed"]:
        done_tasks += 1

""" Create a dictionary for the JSON structure"""
json_data = {employee_id: tasks_list}

""" Write the JSON data to a file"""
file_name = f"{employee_id}.json"
with open(file_name, 'w') as json_file:
    json.dump(json_data, json_file, indent=2)

"""
 Print a message indicating the export is successful
 """
print("Data exported to {}. Employee {} has completed {} out of {} tasks.".format(file_name, employee_name, done_tasks, total_tasks))