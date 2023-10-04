import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 1:
        exit()

    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    tasks = response.json()

    # Create a dictionary to store tasks by user ID
    tasks_by_user = {}

    for task in tasks:
        user_id = task["userId"]
        username = None  # Placeholder for the username

        # Fetch the user's data if not already fetched
        if user_id not in tasks_by_user:
            user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
            user_response = requests.get(user_url)
            user_data = user_response.json()
            username = user_data["username"]
            tasks_by_user[user_id] = []

        # Append task details to the respective user
        tasks_by_user[user_id].append(
            {
                "username": username or tasks_by_user[user_id][0]["username"],
                "task": task["title"],
                "completed": task["completed"],
            }
        )

    # Export tasks to JSON files
    for user_id, user_tasks in tasks_by_user.items():
        with open(f"{user_id}.json", "w") as json_file:
            json.dump({user_id: user_tasks}, json_file, indent=4)

    # Export all tasks to a single JSON file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)
