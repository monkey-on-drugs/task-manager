import json
import os

# 1. Function to load tasks from the JSON file
def load_tasks(file_name="tasks.json"):
    # TODO: Check if the file exists. If it does, load the data. If not, return an empty list.
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []
    return tasks
    pass

# 2. Function to save tasks to the JSON file
def save_tasks(tasks, file_name="tasks.json"):
    # TODO: Save the tasks to the JSON file with proper formatting.
    with open(file_name, 'w') as file:
        json.dump(tasks, file, indent=4)
    pass

# 3. Function to display all tasks
def display_tasks(tasks):
    # TODO: Display all tasks in a readable format. If there are no tasks, print a message saying no tasks are available.
    pass

# 4. Function to add a task
def add_task(tasks):
    # TODO: Get task title, description, and due date from user input.
    # Generate a new task ID by checking the length of the tasks list or use the next available ID.
    pass

# 5. Function to update a task
def update_task(tasks):
    # TODO: Ask for the task ID to update.
    # Check if the task exists, then allow the user to update its title, description, or due date.
    pass

# 6. Function to delete a task
def delete_task(tasks):
    # TODO: Ask for the task ID to delete.
    # If the task exists, remove it from the list.
    pass

# 7. Main program loop
def main():
    # Load existing tasks from the file
    tasks = load_tasks()

    # Main menu loop
    while True:
        print("\n--- Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            # Show tasks
            display_tasks(tasks)
        elif choice == "2":
            # Add a new task
            add_task(tasks)
        elif choice == "3":
            # Update an existing task
            update_task(tasks)
        elif choice == "4":
            # Delete a task
            delete_task(tasks)
        elif choice == "5":
            # Save tasks and exit the program
            save_tasks(tasks)
            print("Exiting the task manager. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()