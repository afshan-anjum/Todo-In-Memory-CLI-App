# Quickstart: Todo Console App

This document provides a quick overview of how to get started with the Todo Console App.

## Running the Application

1.  **Install dependencies:**
    ```sh
    uv pip install -r requirements.txt
    ```
2.  **Run the main application:**
    ```sh
    python src/main.py
    ```

## Using the Application

The application will present you with a menu of options:

1.  **Add Task**: Prompts for a title and description, then adds a new task.
2.  **View All Tasks**: Displays a list of all current tasks.
3.  **Update Task**: Prompts for a task ID and allows you to edit the title and description.
4.  **Delete Task**: Prompts for a task ID and removes the task.
5.  **Mark Task Complete/Incomplete**: Prompts for a task ID and toggles its completion status.
6.  **Exit**: Exits the application.
