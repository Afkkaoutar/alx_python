import json
import requests
import sys

def export_to_json(employee_id):
    """
    Export a user's tasks to a JSON file.

    Args:
        employee_id (int): The employee's ID.

    Returns:
        None
    """
    # Define the API endpoints
    user_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_endpoint = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Make requests to fetch user details and TODO list
    user_response = requests.get(user_endpoint)
    todo_response = requests.get(todo_endpoint)

    # Check if the requests were successful
    if user_response.status_code != 200 or todo_response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return

    # Parse the JSON responses
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Create a list to store the employee's tasks
    employee_tasks = []

    # Populate the list with task information
    for task in todo_data:
        task_info = {
            "task": task["title"],
            "completed": task["completed"],
            "username": user_data["username"]
        }
        employee_tasks.append(task_info)

    # Write the list to a JSON file
    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(employee_tasks, json_file, indent=4)

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
