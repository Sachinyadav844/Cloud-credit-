# Define the To-Do list class
class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the list.")

    def view_tasks(self):
        """Displays all tasks in the list."""
        if not self.tasks:
            print("No tasks in the list.")
            return
        print("\nTo-Do List:")
        for index, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Not Completed"
            print(f"{index}. {task['task']} - {status}")

    def delete_task(self, task_index):
        """Deletes a task by its index."""
        try:
            removed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        except IndexError:
            print("Invalid task number.")

    def mark_completed(self, task_index):
        """Marks a task as completed."""
        try:
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task '{self.tasks[task_index - 1]['task']}' marked as completed.")
        except IndexError:
            print("Invalid task number.")


# Main program to interact with the To-Do list
def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Delete a task")
        print("4. Mark a task as completed")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            todo_list.view_tasks()
        elif choice == "2":
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to delete: "))
                todo_list.delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            todo_list.view_tasks()
            try:
                task_index = int(input("Enter the task number to mark as completed: "))
                todo_list.mark_completed(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "5":
            print("Exiting the To-Do list. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")


# Run the program
if __name__ == "__main__":
    main()
