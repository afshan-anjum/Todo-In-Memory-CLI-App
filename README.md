# Todo In-Memory Python Console App

A command-line todo application built with Python 3.13 that stores tasks in memory. This project uses spec-driven development with Qwen Code and SpecKit Plus, following clean code principles and proper project structure.

## Overview

This is a simple console-based todo application where tasks are stored in memory. The application supports adding, deleting, updating, viewing, and marking tasks as complete or incomplete. Since it's an in-memory application, all tasks will be lost when the application exits.

## Core Principles

This project adheres to the following core principles as defined in the [Project Constitution](.specify/memory/constitution.md):

1.  **Spec-Driven Development**: All features are specified before implementation.
2.  **Clean Code Standards**: The code follows PEP 8 and other clean code guidelines.
3.  **Defined Project Structure**: The project follows a clear and consistent directory structure.
4.  **Technology Constraints**: The project uses Python 3.13 and UV for dependency management, with no external database.

## Features

- Add a new task with a title and optional description.
- Delete a task by its ID.
- Update an existing task's title or description.
- View a list of all tasks with their status.
- Mark a task as complete or incomplete.

## Getting Started

### Prerequisites

- Python 3.13
- UV (a Python package manager)

### Installation

1.  Clone the repository:
    ```sh
    git clone <repository-url>
    cd todo-app
    ```
2.  Install dependencies using UV:
    ```sh
    uv pip install -r requirements.txt
    ```
    *(Note: `requirements.txt` will be created as dependencies are added.)*

### Usage

To run the application, execute the following command from the root directory:

```sh
python src/main.py
```

This will start the interactive console menu.

## Development Workflow

This project uses the **SpecKit Plus** workflow with the Gemini CLI.

1.  **Specify a feature:** Use the `/sp.specify` command to create a feature specification.
2.  **Plan the implementation:** Use the `/sp.plan` command to create a technical plan.
3.  **Break down into tasks:** Use the `/sp.tasks` command to generate a task list.
4.  **Implement the feature:** Use the `/sp.implement` command to execute the tasks.

All development artifacts are stored in the `specs/` and `history/` directories.
