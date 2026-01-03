# Tasks: Todo In-Memory Python Console Application

**Feature**: `001-todo-app`
**Status**: Pending
**Spec**: [spec.md](spec.md) | **Plan**: [plan.md](plan.md)

## Implementation Strategy
- **Approach**: Spec-Driven Development with independent feature phases.
- **MVP Scope**: Phases 1-3 (Setup, Foundations, User Story 1) provides a usable "Add & View" application.
- **Testing**: Pytest for unit testing service logic. Manual verification for Console UI.

## Dependencies
1. **Setup** -> **Foundations** (Blocking)
2. **Foundations** -> **Phase 3 (US1)** (Blocking)
3. **Phase 3 (US1)** -> **Phase 4 (US2)** (Blocking - needs list to select from)
4. **Phase 4 (US2)** -> **Phase 5 (US3)** (Blocking - needs list to select from)

---

## Phase 1: Setup
**Goal**: Initialize project structure and configuration.

- [X] T001 Create project directory structure `src/models`, `src/services`, `src/ui`, `src/utils`, `tests`
- [X] T002 Create `pyproject.toml` with project metadata and dev dependencies (pytest)
- [X] T003 Create `__init__.py` in all `src` subdirectories and `tests`

## Phase 2: Foundational Components
**Goal**: Create core data models and shared utilities.
**Independent Test**: `Task` class can be instantiated and validators work correctly.

- [X] T004 Create `Task` data class in `src/models/task.py` with attributes: id, title, description, created_at, completed, completed_at
- [X] T005 Create validation helpers in `src/utils/validators.py` (validate_title, validate_id)
- [X] T006 [P] Create `TaskService` class skeleton in `src/services/task_service.py` with internal list storage

## Phase 3: User Story 1 - Add and View Tasks (P1)
**Goal**: Users can add tasks and view the list.
**Independent Test**: Run app, add 3 tasks, verify they appear in list.

- [X] T007 [US1] Create unit tests for `add_task` and `get_all_tasks` in `tests/test_task_service.py`
- [X] T008 [US1] Implement `add_task` in `src/services/task_service.py` (auto-gen ID, timestamps)
- [X] T009 [US1] Implement `get_all_tasks` in `src/services/task_service.py`
- [X] T010 [US1] Implement `ConsoleUI` class in `src/ui/console_ui.py` with main loop and "Add"/"View" menu stubs
- [X] T011 [US1] Implement `display_tasks` method in `src/ui/console_ui.py` for formatted output
- [X] T012 [US1] Implement input handling for adding tasks in `src/ui/console_ui.py`
- [X] T013 [US1] Create entry point `src/main.py` to wire UI and Service

## Phase 4: User Story 2 - Complete and Delete Tasks (P2)
**Goal**: Users can mark tasks as done or remove them.
**Independent Test**: Add task, mark complete (check tick), delete it (check gone).

- [X] T014 [US2] Add unit tests for `complete_task` and `delete_task` in `tests/test_task_service.py`
- [X] T015 [US2] Implement `complete_task` in `src/services/task_service.py` (update status and `completed_at`)
- [X] T016 [US2] Implement `delete_task` in `src/services/task_service.py`
- [X] T017 [US2] Update `ConsoleUI` in `src/ui/console_ui.py` to add "Complete" and "Delete" menu options
- [X] T018 [US2] Implement interaction logic for completing and deleting tasks in `src/ui/console_ui.py`

## Phase 5: User Story 3 - Update Task Details (P3)
**Goal**: Users can edit existing tasks.
**Independent Test**: Add task, update title, verify change in list.

- [X] T019 [US3] Add unit tests for `update_task` in `tests/test_task_service.py`
- [X] T020 [US3] Implement `update_task` in `src/services/task_service.py` (handle partial updates)
- [X] T021 [US3] Update `ConsoleUI` in `src/ui/console_ui.py` to add "Update" menu option
- [X] T022 [US3] Implement interaction logic for updating tasks in `src/ui/console_ui.py`

## Phase 6: Polish & Cross-Cutting Concerns
**Goal**: robustness, edge cases, and final verification.

- [X] T023 Implement robust error handling in `ConsoleUI` (catch `ValueError` for non-numeric IDs)
- [X] T024 Review and refine output formatting (tables/spacing) in `src/ui/console_ui.py`
- [X] T025 Run full test suite and ensure >70% coverage
- [X] T026 Verify all PEP 8 standards with linting check