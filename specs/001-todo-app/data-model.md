# Data Model: Todo Application

## Task

Represents a single todo item in the application.

-   **id**: `int` - A unique identifier for the task.
-   **title**: `str` - The title of the task (max 100 characters).
-   **description**: `str` - A more detailed description of the task (max 500 characters).
-   **created_at**: `datetime` - The timestamp when the task was created.
-   **completed**: `bool` - The completion status of the task (default: `False`).
-   **completed_at**: `datetime` or `None` - The timestamp when the task was marked as complete.
