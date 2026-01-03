from src.services.task_service import TaskService
from src.ui.console_ui import ConsoleUI

def main():
    service = TaskService()
    ui = ConsoleUI(service)
    ui.run()

if __name__ == "__main__":
    main()
