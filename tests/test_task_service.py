import pytest
from datetime import datetime
from src.services.task_service import TaskService
from src.models.task import Task

def test_add_task():
    service = TaskService()
    task = service.add_task("Test Task", "Test Description")
    
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert isinstance(task.created_at, datetime)
    assert task.completed is False
    assert len(service.get_all_tasks()) == 1

def test_add_multiple_tasks():
    service = TaskService()
    service.add_task("Task 1")
    service.add_task("Task 2")
    
    tasks = service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].id == 2

def test_add_task_validation():
    service = TaskService()
    with pytest.raises(ValueError, match="Title cannot be empty"):
        service.add_task("")

def test_get_all_tasks_empty():
    service = TaskService()
    assert service.get_all_tasks() == []

def test_complete_task():
    service = TaskService()
    task = service.add_task("Test Task")
    success = service.complete_task(task.id)
    
    assert success is True
    assert task.completed is True
    assert isinstance(task.completed_at, datetime)

def test_complete_task_invalid_id():
    service = TaskService()
    success = service.complete_task(999)
    assert success is False

def test_delete_task():
    service = TaskService()
    task = service.add_task("Test Task")
    success = service.delete_task(task.id)
    
    assert success is True
    assert len(service.get_all_tasks()) == 0

def test_delete_task_invalid_id():
    service = TaskService()
    success = service.delete_task(999)
    assert success is False

def test_update_task():
    service = TaskService()
    task = service.add_task("Old Title", "Old Description")
    success = service.update_task(task.id, title="New Title", description="New Description")
    
    assert success is True
    assert task.title == "New Title"
    assert task.description == "New Description"

def test_update_task_partial():
    service = TaskService()
    task = service.add_task("Old Title", "Old Description")
    success = service.update_task(task.id, title="New Title")
    
    assert success is True
    assert task.title == "New Title"
    assert task.description == "Old Description"

def test_update_task_invalid_id():
    service = TaskService()
    success = service.update_task(999, title="New Title")
    assert success is False
