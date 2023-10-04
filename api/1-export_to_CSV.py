#!/usr/bin/python
"""import requests module"""
import requests
""" Import sys module to get command line arguments"""
import sys
""" import csv"""
import csv

"""
Get the employee ID from the first argument
"""
employee_id = sys.argv[1]
"""
Define the base URL for the API
"""
base_url = "https://jsonplaceholder.typicode.com/users/"

employee = requests.get(base_url + employee_id).json()
employee_name = employee["name"]
todos = requests.get(base_url + employee_id + "/todos").json()

"""Initialize the total and done tasks counters"""
total_tasks = 0
done_tasks = 0
"""Initialize an empty list for the done tasks titles"""
done_tasks_titles = []
"""Loop through the todos list and update the counters and titles list"""
for todo in todos:
    total_tasks += 1
    if todo["completed"]:
        done_tasks += 1
        done_tasks_titles.append(todo["title"])

"""Define the CSV filename"""
csv_filename = "{}.csv".format(employee_id)

""" Write data to CSV file"""
with open(csv_filename, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
    
    """ Write header"""
    csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    """ Write rows"""
    for title in done_tasks_titles:
        csv_writer.writerow([employee_id, employee_name, "True", title])

    for i in range(total_tasks - done_tasks):
        csv_writer.writerow([employee_id, employee_name, "False", todos[i]["title"]])

print("Employee {} tasks exported to {}".format(employee_name, csv_filename))