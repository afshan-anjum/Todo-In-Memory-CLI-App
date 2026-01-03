<!--
Sync Impact Report:
Version change: None -> 1.0.0
Modified principles: All principles updated with detailed content from user input.
Added sections: Project Overview, Feature Requirements, Data Model, User Interface Guidelines, Code Quality Requirements, Development Workflow, Git Commit Standards, Non-Functional Requirements, Constraints and Limitations, Success Criteria, Deliverable Checklist, Review and Updates.
Removed sections: None (template placeholders replaced).
Templates requiring updates:
- .specify/templates/plan-template.md (⚠ pending)
- .specify/templates/spec-template.md (⚠ pending)
- .specify/templates/tasks-template.md (⚠ pending)
- .gemini/commands/*.toml (⚠ pending)
- README.md (⚠ pending)
- Gemini.md (⚠ pending)
Follow-up TODOs: Ensure alignment of constitution principles with linked templates and documentation.
-->
# Todo In-Memory Python Console App Constitution

## Project Overview
A command-line todo application built with Python 3.13 that stores tasks in memory. This project uses spec-driven development with Qwen Code and SpecKit Plus, following clean code principles and proper project structure.

## Core Principles

### 1. Spec-Driven Development
- All features must be specified before implementation
- Specifications must be written in clear, testable language
- Each specification should be atomic and focused on a single feature
- All specifications are stored in /spec_history folder
- Specifications follow the SpecKit Plus format and conventions

### 2. Clean Code Standards
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Keep functions small and focused (single responsibility)
- Write self-documenting code with minimal but clear comments
- Use type hints for function parameters and return values
- Maximum function length: 20-25 lines
- Maximum file length: 300 lines

### 3. Project Structure

```
todo-app/
├── constitution.md
├── spec_history/
│   ├── spec_001_add_task.md
│   ├── spec_002_delete_task.md
│   └── ...
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py
│   ├── ui/
│   │   ├── __init__.py
│   │   └── console_ui.py
│   └── utils/
│       ├── __init__.py
│       └── validators.py
├── tests/
│   ├── __init__.py
│   └── test_task_service.py
├── README.md
├── Gemini.md
└── pyproject.toml
```

### 4. Technology Constraints
- *Python Version*: Must use Python 3.13
- *Package Manager*: UV for dependency management
- *No External Database*: All data stored in memory (Python data structures)
- *No External Dependencies*: Minimize external libraries; use standard library where possible
- *Console Only*: No GUI, web interface, or API

## Feature Requirements

### Basic Level Features (Must Implement All)

#### 1. Add Task
- Create new todo items with unique ID
- Required fields: title (string, max 100 chars)
- Optional fields: description (string, max 500 chars)
- Auto-generate unique task ID (integer or UUID)
- Auto-set creation timestamp
- Default status: incomplete
- Validate input before adding
- Provide clear success/error messages

#### 2. Delete Task
- Remove task by ID
- Confirm task exists before deletion
- Provide confirmation message
- Handle invalid ID gracefully
- Cannot be undone (warn user)

#### 3. Update Task
- Modify existing task by ID
- Allow updating: title, description
- Cannot modify: ID, creation date, completion status (use Mark Complete for status)
- Validate updated data
- Preserve original creation timestamp
- Provide clear success/error messages

#### 4. View Task List
- Display all tasks in a readable format
- Show: ID, title, status (✓ or ✗), creation date
- Display tasks in order of creation (newest first optional)
- Handle empty list gracefully ("No tasks found")
- Use clear visual formatting (tables or structured lists)

#### 5. Mark as Complete/Incomplete
- Toggle task completion status by ID
- Show clear status indicators (✓ complete / ✗ incomplete)
- Record completion timestamp when marked complete
- Allow toggling back to incomplete
- Validate task exists before toggling

## Data Model

### Task Object
```python
{
    "id": int or str,  # Unique identifier
    "title": str,  # Required, max 100 chars
    "description": str,  # Optional, max 500 chars
    "created_at": datetime,  # Auto-generated
    "completed": bool,  # Default False
    "completed_at": datetime or None  # Set when marked complete
}
```

## User Interface Guidelines

### Console Menu Structure

```
=== Todo Application ===
1. Add Task
2. View All Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete/Incomplete
6. Exit

Enter your choice (1-6):
```

### Input/Output Standards
- Clear prompts for user input
- Validate all user inputs
- Display helpful error messages
- Confirm destructive actions (delete)
- Show success messages after operations
- Use consistent formatting throughout

## Code Quality Requirements

### Error Handling
- Use try-except blocks for user input
- Validate all data before processing
- Provide meaningful error messages
- Never crash on invalid input
- Log errors when appropriate

### Testing Approach
- Write unit tests for core business logic
- Test edge cases (empty list, invalid IDs, etc.)
- Test input validation
- Aim for >70% code coverage

### Documentation
- Docstrings for all classes and functions (Google or NumPy style)
- README.md with setup and usage instructions
- Gemini.md with Gemini CLI workflow and commands
- Inline comments only for complex logic

## Development Workflow

### With Gemini CLI and SpecKit Plus
1. Write specification for feature in /spec_history
2. Use Gemini CLI to generate implementation from spec
3. Review and refine generated code
4. Test the implementation
5. Commit spec and code together
6. Repeat for next feature

### Git Commit Standards
- Commit spec and implementation together
- Use conventional commit messages: feat:, fix:, docs:, refactor:
- Reference spec file in commit message
- Keep commits atomic and focused

## Non-Functional Requirements

### Performance
- Instant response for all operations (in-memory)
- Handle up to 1000 tasks efficiently

### Usability
- Intuitive menu navigation
- Clear instructions at each step
- Minimal keystrokes for common operations

### Maintainability
- Modular code structure (models, services, UI separated)
- Easy to add new features
- Well-documented code

## Constraints and Limitations

### Explicit Constraints
- No data persistence (tasks lost on exit)
- Single-user application
- Console interface only
- No authentication/authorization
- No task categories, tags, or priorities (basic level)
- No task scheduling or reminders

### Future Considerations (Out of Scope for Basic Level)
- File-based persistence
- Task priorities or categories
- Due dates and reminders
- Search and filter functionality
- Task sorting options

## Success Criteria

The project is complete when:
- ✅ All 5 basic features are implemented and working
- ✅ All specifications are documented in /spec_history
- ✅ Code follows clean code principles
- ✅ Project structure matches defined layout
- ✅ README.md and QWEN.md are complete
- ✅ Application runs without crashes
- ✅ User can perform all CRUD operations successfully
- ✅ Code is committed to GitHub repository

## Deliverable Checklist

- [ ] constitution.md - This file
- [ ] /spec_history folder with all specification files
- [ ] /src folder with complete source code
- [ ] README.md with setup instructions
- [ ] Gemini.md with Qwen Code instructions
- [ ] Working console application
- [ ] GitHub repository with all files

## Review and Updates

This constitution may be updated during development if:
- Critical technical constraints are discovered
- Gemini CLI/SpecKit Plus best practices evolve
- Team consensus identifies necessary changes

All updates must be documented and committed to version control.

## Governance
This constitution supersedes all other practices; Amendments require documentation, approval, migration plan. All PRs/reviews must verify compliance; Complexity must be justified; Use relevant guidance files for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2026-01-02 | **Last Amended**: 2026-01-02