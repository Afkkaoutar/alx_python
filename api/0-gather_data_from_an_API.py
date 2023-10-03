import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # Define the API endpoints
    user_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_endpoint = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

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

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todo_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_num_tasks = len(todo_data)

    # Print employee TODO list progress
    print(f"Employee {user_data['name']} is done with tasks({num_completed_tasks}/{total_num_tasks}):")

    # Print titles of completed tasks
    for task in completed_tasks:
        print(f"    {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_list_progress(employee_id)
