import pytest
from utils.validation import validate_profile_data

@pytest.mark.parametrize("first_name, last_name, student_id, expected",
    [
        #Valid partition
        ("Alice", "Smith", "12345678", None),
        # Missing first_name
        ("", "Smith", "12345678", "All fields are required."),
        # Missing last_name
        ("Alice", "", "12345678", "All fields are required."),
        # Missing student_id
        ("Alice", "Smith", "", "All fields are required."),
        # incorrect student_id
        ("Alice", "Smith", "1234", "Invalid Student ID"),
        # None value
        (None, "Smith", "12345678", "All fields are required."),
        # White-space only
        ("  ", " ", "      ", "All fields are required."),
        # All empty
        ("", "", "", "All fields are required."),
    ]
)
def test_validate_profile(first_name, last_name, student_id, expected):
    assert validate_profile_data(first_name, last_name, student_id) == expected