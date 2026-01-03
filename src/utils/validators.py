def validate_title(title: str) -> str:
    """
    Validates the task title.
    Raises ValueError if title is empty or exceeds 100 characters.
    """
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    
    cleaned_title = title.strip()
    if len(cleaned_title) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    
    return cleaned_title

def validate_description(description: str) -> str:
    """
    Validates the task description.
    Raises ValueError if description exceeds 500 characters.
    """
    if not description:
        return ""
        
    cleaned_description = description.strip()
    if len(cleaned_description) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    
    return cleaned_description

def validate_id(task_id: str) -> int:
    """
    Validates that the task_id is a positive integer.
    Raises ValueError if invalid.
    """
    try:
        id_val = int(task_id)
    except ValueError:
        raise ValueError("Task ID must be a number.")
    
    if id_val <= 0:
        raise ValueError("Task ID must be a positive integer.")
    
    return id_val
