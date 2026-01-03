# Gemini CLI Workflow for the Todo App

This document outlines how to use the Gemini CLI with the SpecKit Plus toolkit to develop the Todo In-Memory Python Console App.

## Development Process

The development process follows a strict Spec-Driven Development (SDD) workflow. All work is initiated through Gemini CLI commands, which create and update the necessary artifacts to guide implementation.

The core workflow is as follows:

1.  **`/sp.specify`**: Define a new feature in plain English. This generates a detailed `spec.md` file.
2.  **`/sp.plan`**: Create a technical plan based on the specification. This generates a `plan.md` and other design artifacts.
3.  **`/sp.tasks`**: Break down the plan into a list of actionable tasks. This generates a `tasks.md` file.
4.  **`/sp.implement`**: Execute the tasks to implement the feature.

## Key Commands

### 1. `/sp.specify`

Use this command to create a new feature specification.

**Example:**

```
/sp.specify "Add a feature to mark tasks as high priority"
```

This will create a new feature directory in `specs/` with a `spec.md` file that defines the requirements for the priority feature.

### 2. `/sp.plan`

Once a specification is created, use this command to generate a technical plan.

**Example:**

```
/sp.plan
```

This will read the `spec.md` for the current feature and create a `plan.md` outlining the architecture, data models, and implementation strategy.

### 3. `/sp.tasks`

After the plan is created, use this command to generate a list of implementation tasks.

**Example:**

```
/sp.tasks
```

This will create a `tasks.md` file with a detailed, dependency-ordered list of tasks required to implement the feature.

### 4. `/sp.implement`

With a task list in place, use this command to start the implementation.

**Example:**

```
/sp.implement
```

The agent will execute the tasks in `tasks.md` in the correct order, writing code and tests as defined.

## Project Constitution

All development must adhere to the principles outlined in the [Project Constitution](.specify/memory/constitution.md). This document is the authoritative source for project standards, including code style, project structure, and technology constraints.

Before starting any new work, ensure you are familiar with the constitution. The `/sp.analyze` command can be used to check for any inconsistencies between your proposed changes and the constitution.
