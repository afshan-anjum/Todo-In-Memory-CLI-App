import pytest
from src.utils.validators import validate_title, validate_description, validate_id

def test_validate_title_valid():
    assert validate_title("  Valid Title  ") == "Valid Title"

def test_validate_title_empty():
    with pytest.raises(ValueError, match="Title cannot be empty"):
        validate_title("")
    with pytest.raises(ValueError, match="Title cannot be empty"):
        validate_title("   ")

def test_validate_title_too_long():
    with pytest.raises(ValueError, match="Title cannot exceed 100 characters"):
        validate_title("a" * 101)

def test_validate_description_valid():
    assert validate_description("  Valid Desc  ") == "Valid Desc"
    assert validate_description("") == ""
    assert validate_description(None) == ""

def test_validate_description_too_long():
    with pytest.raises(ValueError, match="Description cannot exceed 500 characters"):
        validate_description("a" * 501)

def test_validate_id_valid():
    assert validate_id("123") == 123

def test_validate_id_non_numeric():
    with pytest.raises(ValueError, match="Task ID must be a number"):
        validate_id("abc")

def test_validate_id_zero_or_negative():
    with pytest.raises(ValueError, match="Task ID must be a positive integer"):
        validate_id("0")
    with pytest.raises(ValueError, match="Task ID must be a positive integer"):
        validate_id("-5")
