import json  # Import the JSON module for handling JSON data
import os    # Import the OS module for file path operations

class TodoList:
    def __init__(self, filename='todolist.json'):
        """
        Initializes the TodoList with a specified filename.
        Loads existing tasks from the file if it exists.
        """
        self.filename = filename
        self.tasks = self.load_tasks()  # Load tasks when the object is created

    def load_tasks(self):
        """
        Loads tasks from the JSON file if it exists.
        Returns an empty list if the file does not exist.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)  # Load tasks from the file
        return []  # Return an empty list if no file is found

    def save_tasks(self):
        """
        Saves the current list of tasks to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)  # Write tasks to the file in JSON format

    def add_task(self, task):
        """
        Adds a new task to the list and saves the updated list.
        """
        self.tasks.append(task)  # Append the new task to the tasks list
        self.save_tasks()  # Save the updated tasks list
        print(f'Task "{task}" added.')  # Confirmation message

    def view_tasks(self):
        """
        Displays the current list of tasks.
        """
        if not self.tasks:  # Check if the task list is empty
            print("No tasks available.")  # Inform the user if there are no tasks
            return
        print("Your tasks:")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")  # Display each task with its index

    def update_task(self, index, new_task):
        """
        Updates an existing task with a new value.
        """
        if 0 <= index < len(self.tasks):  # Check if the index is valid
            self.tasks[index] = new_task  # Update the task at the specified index
            self.save_tasks()  # Save the updated tasks list
            print(f'Task updated to "{new_task}".')  # Confirmation message
        else:
            print("Invalid task number.")  # Inform the user if the index is invalid

    def delete_task(self, index):
        """
        Deletes a task from the list based on the given index.
        """
        if 0 <= index < len(self.tasks):  # Check if the index is valid
            removed_task = self.tasks.pop(index)  # Remove the task and store it
            self.save_tasks()  # Save the updated tasks list
            print(f'Task "{removed_task}" deleted.')  # Confirmation message
        else:
            print("Invalid task number.")  # Inform the user if the index is invalid

def main():
    """
    The main function to run the To-Do List application.
    Provides a command-line interface for user interaction.
    """
    todo_list = TodoList()  # Create a TodoList object
    
    while True:
        # Display the menu options to the user
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Select an option (1-5): ")  # Get user input for the menu choice

        if choice == '1':
            task = input("Enter the task: ")  # Prompt the user to enter a task
            todo_list.add_task(task)  # Add the new task
        elif choice == '2':
            todo_list.view_tasks()  # Display current tasks
        elif choice == '3':
            todo_list.view_tasks()  # Show tasks before updating
            task_number = int(input("Enter the task number to update: ")) - 1  # Get task index
            new_task = input("Enter the new task: ")  # Get the new task description
            todo_list.update_task(task_number, new_task)  # Update the specified task
        elif choice == '4':
            todo_list.view_tasks()  # Show tasks before deletion
            task_number = int(input("Enter the task number to delete: ")) - 1  # Get task index
            todo_list.delete_task(task_number)  # Delete the specified task
        elif choice == '5':
            print("Exiting the application.")  # Inform user before exiting
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please try again.")  # Handle invalid menu choices

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
