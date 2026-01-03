import sys
from src.services.task_service import TaskService
from src.utils.validators import validate_id

class ConsoleUI:
    def __init__(self, service: TaskService):
        self.service = service

    def display_menu(self):
        print("\n--- TODO APP ---")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Update Task")
        print("6. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                self.add_task_ui()
            elif choice == "2":
                self.view_tasks_ui()
            elif choice == "3":
                self.complete_task_ui()
            elif choice == "4":
                self.delete_task_ui()
            elif choice == "5":
                self.update_task_ui()
            elif choice == "6":
                print("Goodbye!")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

    def add_task_ui(self):
        print("\n--- Add New Task ---")
        title = input("Title: ")
        description = input("Description (optional): ")
        try:
            task = self.service.add_task(title, description)
            print(f"Task added successfully! ID: {task.id}")
        except ValueError as e:
            print(f"Error: {e}")

    def view_tasks_ui(self):
        tasks = self.service.get_all_tasks()
        if not tasks:
            print("\nNo tasks found.")
            return

        print("\n--- Task List ---")
        print(f"{ 'ID':<4} | {'Status':<8} | {'Title':<30}")
        print("-" * 50)
        for task in tasks:
            status = "[✓]" if task.completed else "[ ]"
            print(f"{task.id:<4} | {status:<8} | {task.title:<30}")

    def complete_task_ui(self):
        print("\n--- Complete Task ---")
        task_id_str = input("Enter Task ID to mark as complete: ")
        try:
            task_id = validate_id(task_id_str)
            if self.service.complete_task(task_id):
                print(f"Task {task_id} marked as complete.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def delete_task_ui(self):
        print("\n--- Delete Task ---")
        task_id_str = input("Enter Task ID to delete: ")
        try:
            task_id = validate_id(task_id_str)
            if self.service.delete_task(task_id):
                print(f"Task {task_id} deleted successfully.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")

    def update_task_ui(self):
        print("\n--- Update Task ---")
        task_id_str = input("Enter Task ID to update: ")
        try:
            task_id = validate_id(task_id_str)
            print("Leave blank to keep current value.")
            new_title = input("New Title: ").strip()
            new_desc = input("New Description: ").strip()
            
            title = new_title if new_title else None
            description = new_desc if new_desc else None
            
            if self.service.update_task(task_id, title, description):
                print(f"Task {task_id} updated successfully.")
            else:
                print(f"Error: Task with ID {task_id} not found.")
        except ValueError as e:
            print(f"Error: {e}")