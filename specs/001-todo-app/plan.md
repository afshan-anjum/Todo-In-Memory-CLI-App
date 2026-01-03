# Implementation Plan: Todo Console App

**Branch**: `001-todo-app` | **Date**: 2026-01-02 | **Spec**: [spec.md](specs/001-todo-app/spec.md)
**Input**: Feature specification from `specs/001-todo-app/spec.md`

## Summary

This plan outlines the implementation of a console-based todo application. It will be built in six sequential phases, starting with project setup, then foundational components, followed by implementing the three user stories (Add/View, Complete/Delete, Update), and finishing with polish and cross-cutting concerns. The architecture will be layered to separate concerns, and development will adhere to the project constitution.

## Technical Context

**Language/Version**: Python 3.13
**Primary Dependencies**: None (Standard Library)
**Storage**: In-memory Python data structures
**Testing**: pytest
**Target Platform**: Console
**Project Type**: Single project
**Performance Goals**: Instant response for all operations (in-memory); Handle up to 1000 tasks efficiently
**Constraints**: No data persistence; Single-user application; Console interface only
**Scale/Scope**: Up to 1000 tasks

## Constitution Check

- [X] **Spec-Driven Development**: All features specified before implementation in spec.md
- [X] **Clean Code Standards**: Adherence to PEP 8 and clean code guidelines with type hints
- [X] **Project Structure**: Following the defined single-project layout
- [X] **Technology Constraints**: Using Python 3.13, UV package manager, and no external database
- [X] **Testing Requirements**: pytest for unit tests with >70% coverage target

## Project Structure
```text
todo-app/
├── constitution.md              # Project governance rules
├── specs/
│   └── 001-todo-app/
│       ├── spec.md              # Feature specification
│       ├── plan.md              # This implementation plan
│       └── tasks.md             # Detailed task breakdown
├── src/
│   ├── __init__.py
│   ├── main.py                  # Application entry point
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py              # Task data model
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py      # Business logic layer
│   ├── ui/
│   │   ├── __init__.py
│   │   └── console_ui.py        # User interface layer
│   └── utils/
│       ├── __init__.py
│       └── validators.py        # Input validation utilities
├── tests/
│   ├── __init__.py
│   └── test_task_service.py     # Unit tests
├── README.md                     # Setup and usage instructions
├── QWEN.md                       # Qwen code integration guide
└── pyproject.toml               # Project configuration
```

**Structure Decision**: The project follows the 'Single project' structure as defined in the constitution, with clear separation of concerns using a layered architecture.

## Architecture Decisions

### Layered Architecture
```
┌─────────────────────────────────┐
│      Presentation Layer         │  console_ui.py
│  (User Input/Output Handling)   │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│       Service Layer             │  task_service.py
│   (Business Logic & CRUD)       │
└────────────┬────────────────────┘
             │
┌────────────▼────────────────────┐
│         Model Layer             │  task.py
│     (Data Structures)           │
└─────────────────────────────────┘
             │
┌────────────▼────────────────────┐
│       Storage Layer             │  In-memory list
│    (Data Persistence)           │
└─────────────────────────────────┘
```

**Decision Rationale**:
1. **Separation of Concerns**: UI logic separate from business logic
2. **Testability**: Service layer can be unit tested independently
3. **Maintainability**: Changes to UI don't affect core logic
4. **Scalability**: Easy to swap storage layer (e.g., file/database) later

### Data Model Design

**Task Entity**:
```python
@dataclass
class Task:
    id: int
    title: str
    description: str
    created_at: datetime
    completed: bool = False
    completed_at: Optional[datetime] = None
```

**Decision Rationale**:
- Using `dataclass` for automatic `__init__`, `__repr__`, and `__eq__`
- Immutable IDs prevent accidental modification
- Timestamp tracking for audit trail
- Optional `completed_at` only set when task is marked complete

### Storage Strategy

**In-Memory List**:
```python
class TaskService:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1
```

**Decision Rationale**:
- Simple list provides O(n) search, sufficient for 1000 tasks
- Sequential ID generation ensures uniqueness
- No external dependencies or file I/O complexity
- Meets performance goals (<100ms operations)

### Error Handling Strategy

**Validation at UI Layer**:
- Check for empty inputs
- Validate ID format (numeric)
- Confirm destructive operations

**Service Layer Responses**:
- Return `None` for not-found scenarios
- Raise `ValueError` for invalid data
- Let UI handle user-facing error messages

**Decision Rationale**:
- Fail fast with clear error messages
- Don't crash on invalid input
- Service layer stays clean, UI handles presentation

## Implementation Phases

### Phase 1: Setup (T001-T003)
**Goal**: Initialize project structure and configuration
**Duration**: 15 minutes
**Dependencies**: None

**Tasks**:
1. Create directory structure (`src/`, `tests/`, subdirectories)
2. Create `pyproject.toml` with pytest dependency
3. Create all `__init__.py` files

**Verification**: Run `uv run python -c "import src"` without errors

---

### Phase 2: Foundational Components (T004-T006)
**Goal**: Build core data model and service skeleton
**Duration**: 30 minutes
**Dependencies**: Phase 1

**Tasks**:
1. Implement `Task` dataclass with all attributes
2. Create validation utilities (title length, ID format)
3. Create `TaskService` class skeleton with storage list

**Verification**: 
```python
from src.models.task import Task
from src.services.task_service import TaskService

task = Task(1, "Test", "Description", datetime.now())
service = TaskService()
assert service._tasks == []
```

---

### Phase 3: User Story 1 - Add and View Tasks (T007-T013)
**Goal**: Implement core "Add" and "View" functionality
**Duration**: 1 hour
**Dependencies**: Phase 2
**Priority**: P1 (MVP)

**Tasks**:
1. Write unit tests for `add_task()` and `get_all_tasks()`
2. Implement `add_task()` with ID auto-generation
3. Implement `get_all_tasks()` returning task list
4. Create `ConsoleUI` class with main menu loop
5. Implement `display_tasks()` with formatted output
6. Implement `add_task_ui()` for user input handling
7. Create `main.py` entry point

**Verification**: 
- Run tests: `uv run pytest tests/test_task_service.py -v`
- Manual test: Add 3 tasks, verify they appear in list with IDs

**Success Criteria**: SC-001 (Add/View operations functional)

---

### Phase 4: User Story 2 - Complete and Delete Tasks (T014-T018)
**Goal**: Implement task completion and deletion
**Duration**: 45 minutes
**Dependencies**: Phase 3
**Priority**: P2

**Tasks**:
1. Write unit tests for `complete_task()` and `delete_task()`
2. Implement `complete_task()` updating status and timestamp
3. Implement `delete_task()` removing from list
4. Add "Complete" and "Delete" menu options to UI
5. Implement interaction handlers in UI

**Verification**:
- Run tests: `uv run pytest tests/test_task_service.py::test_complete_task -v`
- Manual test: Add task, mark complete (see ✓), delete it (verify gone)

**Success Criteria**: SC-001 (Complete/Delete operations functional)

---

### Phase 5: User Story 3 - Update Task Details (T019-T022)
**Goal**: Implement task editing capability
**Duration**: 30 minutes
**Dependencies**: Phase 4
**Priority**: P3

**Tasks**:
1. Write unit tests for `update_task()`
2. Implement `update_task()` with partial update support
3. Add "Update" menu option to UI
4. Implement update interaction handler

**Verification**:
- Run tests: `uv run pytest tests/test_task_service.py::test_update_task -v`
- Manual test: Add task, update title, verify change in list

**Success Criteria**: SC-001 (All CRUD operations functional)

---

### Phase 6: Polish & Cross-Cutting Concerns (T023-T026)
**Goal**: Ensure robustness, code quality, and edge case handling
**Duration**: 45 minutes
**Dependencies**: Phases 3, 4, 5

**Tasks**:
1. Implement robust error handling for invalid inputs
2. Refine output formatting (tables, alignment, colors)
3. Run full test suite and verify >70% coverage
4. Run linter to ensure PEP 8 compliance

**Verification**:
- Coverage: `uv run pytest --cov=src --cov-report=term`
- Linting: `uv run ruff check src/`
- Manual testing of all edge cases from spec.md

**Success Criteria**: SC-002 (Performance), SC-003 (Coverage), SC-004 (No crashes), SC-005 (Code quality)

## Testing Strategy

### Unit Tests (pytest)
**Scope**: Service layer logic
**Location**: `tests/test_task_service.py`
**Coverage Target**: >70%

**Test Cases**:
```python
def test_add_task_generates_unique_ids()
def test_add_task_validates_title_length()
def test_get_all_tasks_returns_empty_list_initially()
def test_complete_task_updates_status_and_timestamp()
def test_delete_task_removes_from_list()
def test_update_task_modifies_existing_task()
def test_operations_handle_invalid_ids()
```

### Integration Tests (Manual)
**Scope**: End-to-end user journeys
**Method**: Console interaction

**Test Scenarios**:
1. Add 3 tasks → View list → Verify all 3 appear with IDs
2. Add task → Mark complete → Verify ✓ status
3. Add task → Delete → Verify removed from list
4. Add task → Update title → Verify change persists
5. Try invalid inputs (empty title, non-numeric ID) → Verify graceful error handling

### Performance Tests
**Scope**: Verify <100ms response time with 1000 tasks
```python
def test_performance_with_1000_tasks():
    service = TaskService()
    for i in range(1000):
        service.add_task(f"Task {i}", f"Description {i}")
    
    import time
    start = time.time()
    service.get_all_tasks()
    elapsed = time.time() - start
    assert elapsed < 0.1  # 100ms
```

## Risk Analysis

### Technical Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Memory overflow with many tasks | High | Low | Limit to 1000 tasks, add warning at 900 |
| Invalid user input crashes app | High | Medium | Comprehensive validation and try-catch blocks |
| Poor performance with large lists | Medium | Low | Use list comprehensions, avoid nested loops |
| Type errors without proper hints | Low | Medium | Use type hints everywhere, run mypy |

### Process Risks

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Scope creep (persistence, multi-user) | Medium | High | Strict adherence to spec, defer to future phases |
| Insufficient testing coverage | Medium | Medium | Write tests before implementation (TDD approach) |
| PEP 8 violations | Low | Low | Use automated linter (ruff/black) |

## Rollout Plan

### MVP Definition
**Phases 1-3 Complete**: Add and View functionality
- Users can create tasks and see them in a list
- Sufficient for basic todo tracking
- Delivers immediate value

### Full Feature Set
**Phases 1-5 Complete**: All CRUD operations
- Complete task lifecycle management
- Meets all functional requirements (FR-001 to FR-008)

### Production Ready
**Phase 6 Complete**: Polished and tested
- Robust error handling
- High code quality and test coverage
- Ready for handoff or deployment

## Dependencies & Prerequisites

### External Dependencies
- **Python 3.13**: Runtime environment
- **UV**: Package manager and task runner
- **pytest**: Testing framework

### Internal Dependencies
```
Phase 1 (Setup)
    ↓
Phase 2 (Foundations)
    ↓
Phase 3 (Add/View) ← MVP boundary
    ↓
Phase 4 (Complete/Delete)
    ↓
Phase 5 (Update)
    ↓
Phase 6 (Polish)
```

**Blocking Dependencies**:
- Phase 2 blocks Phase 3 (need Task model and service skeleton)
- Phase 3 blocks Phases 4-5 (need list to select tasks from)
- Phases 3-5 block Phase 6 (need features to test)

## Success Metrics

### Code Quality Metrics
- **Test Coverage**: >70% (measured by pytest-cov)
- **Linting**: 0 errors, <5 warnings (measured by ruff)
- **Type Coverage**: 100% (all functions have type hints)

### Functional Metrics
- **Operations Implemented**: 5/5 (Add, View, Update, Delete, Complete)
- **Edge Cases Handled**: 5/5 (from spec.md)
- **User Stories Completed**: 3/3 (US1, US2, US3)

### Performance Metrics
- **Response Time**: <100ms for all operations with 1000 tasks
- **Crash Rate**: 0 crashes during standard user journeys

## Timeline Estimate

| Phase | Duration | Cumulative |
|-------|----------|------------|
| Phase 1: Setup | 15 min | 15 min |
| Phase 2: Foundations | 30 min | 45 min |
| Phase 3: Add/View (MVP) | 1 hour | 1h 45min |
| Phase 4: Complete/Delete | 45 min | 2h 30min |
| Phase 5: Update | 30 min | 3 hours |
| Phase 6: Polish | 45 min | **3h 45min** |

**Total Estimated Time**: ~4 hours for full implementation

---

**Next Steps**: 
1. Review and approve this plan
2. Proceed to [tasks.md](specs/001-todo-app/tasks.md) for detailed task breakdown
3. Begin Phase 1 implementation