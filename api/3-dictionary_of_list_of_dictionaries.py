import json
import requests

def fetch_users():
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    users = response.json()
    return {user["id"]: user["username"] for user in users}

def fetch_tasks():
    tasks_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(tasks_url)
    tasks = response.json()
    return tasks

if __name__ == "__main__":
    users = fetch_users()
    tasks = fetch_tasks()

    # Create a dictionary to store tasks by user ID
    tasks_by_user = {}

    for task in tasks:
        user_id = task["userId"]
        username = users.get(user_id, None)

        if user_id not in tasks_by_user:
            tasks_by_user[user_id] = []

        tasks_by_user[user_id].append(
            {
                "username": username,
                "task": task["title"],
                "completed": task["completed"],
            }
        )

    # Export all tasks to a single JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)
