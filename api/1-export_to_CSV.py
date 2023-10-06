import requests
import csv

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    employee_endpoint = f"{base_url}/users/{employee_id}"
    todo_endpoint = f"{base_url}/todos?userId={employee_id}"

    # Fetch employee details
    employee_response = requests.get(employee_endpoint)
    employee_data = employee_response.json()
    user_id = employee_data["id"]
    username = employee_data["username"]

    # Fetch TODO list
    todo_response = requests.get(todo_endpoint)
    todo_data = todo_response.json()

    # Create a CSV file for the employee
    csv_filename = f"{user_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the CSV header
        writer.writeheader()

        # Write TODO list data to the CSV file
        for task in todo_data:
            writer.writerow({
                "USER_ID": user_id,
            })