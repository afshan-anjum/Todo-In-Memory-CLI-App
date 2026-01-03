from typing import List, Optional
from datetime import datetime
from src.models.task import Task
from src.utils.validators import validate_title, validate_description

class TaskService:
    def __init__(self):
        self._tasks: List[Task] = []
        self._next_id: int = 1

    def _generate_id(self) -> int:
        task_id = self._next_id
        self._next_id += 1
        return task_id

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Adds a new task to the service.
        """
        validated_title = validate_title(title)
        validated_description = validate_description(description)
        
        task = Task(
            id=self._generate_id(),
            title=validated_title,
            description=validated_description,
            created_at=datetime.now()
        )
        self._tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks.
        """
        return self._tasks

    def complete_task(self, task_id: int) -> bool:
        """
        Marks a task as complete. Returns True if successful, False if task not found.
        """
        for task in self._tasks:
            if task.id == task_id:
                task.completed = True
                task.completed_at = datetime.now()
                return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Deletes a task. Returns True if successful, False if task not found.
        """
        for i, task in enumerate(self._tasks):
            if task.id == task_id:
                self._tasks.pop(i)
                return True
        return False

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Updates a task. Returns True if successful, False if task not found.
        Only updates fields that are not None.
        """
        for task in self._tasks:
            if task.id == task_id:
                if title is not None:
                    task.title = validate_title(title)
                if description is not None:
                    task.description = validate_description(description)
                return True
        return False
