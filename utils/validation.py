from __future__ import annotations
import re
from flask import jsonify, request


def validate_profile_data(first_name: str, last_name: str, student_id: str):
    """Validate that required profile fields are present and well-formed."""
    if not first_name or not last_name or not student_id:
        return "All fields are required."
    if first_name.isspace() or last_name.isspace() or student_id.isspace():
        return "All fields are required."
    if not re.match(r"^[A-Za-z0-9]{8,9}$", student_id):
        return "Invalid Student ID"
    return None


def normalize_profile_data(first_name: str, last_name: str, student_id: str):
    """Normalize profile field values (strip whitespace, stringify student_id)."""
    if not first_name or not last_name or not student_id:
        return "All fields are required."

    return {
        "first_name": first_name.strip() if first_name else "",
        "last_name": last_name.strip() if last_name else "",
        "student_id": str(student_id).strip() if student_id else "",
    }


def require_json_content_type():
    """Ensure the request is JSON; returns an error response tuple if not."""
    if not request.is_json:
        return jsonify({"error": "Content-Type must be application/json"}), 415
    return None
