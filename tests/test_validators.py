import pytest
from utils.validation import validate_profile_data
from utils.validation import normalize_profile_data
#validation
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



@pytest.mark.parametrize("first_name, last_name, student_id, expected",
    [
        #Valid partition
        ("Alice", "Smith", "12345678", {
        "first_name": "Alice",
        "last_name": "Smith",
        "student_id": "12345678",
        }),
        # None test
        (None, "Smith", "12345678", "All fields are required."),
        # second None test
        ("Alice", None, "12345678", "All fields are required."),
        # Conversion to string
        ("Alice", "Smith", 12345678, {
        "first_name": "Alice",
        "last_name": "Smith",
        "student_id": "12345678",
        }),
        # Whitespace stripping
        ("Alice   ", "  Smith", "  12345678 ", {
        "first_name": "Alice",
        "last_name": "Smith",
        "student_id": "12345678",
        }),
    ]
)
def test_normalize_profile(first_name, last_name, student_id, expected):
    assert normalize_profile_data(first_name, last_name, student_id) == expected