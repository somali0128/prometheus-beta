import re
import pytest
from src.uuid_generator import generate_uuid

def test_generate_uuid():
    """
    Test that generate_uuid() returns a valid UUID v4 string.
    """
    # Generate a UUID
    generated_uuid = generate_uuid()
    
    # Check that the UUID is a string
    assert isinstance(generated_uuid, str), "UUID should be a string"
    
    # UUID v4 regex pattern
    uuid_pattern = r'^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$'
    
    # Check that the UUID matches the v4 pattern
    assert re.match(uuid_pattern, generated_uuid, re.IGNORECASE), "Generated UUID does not match UUID v4 format"

def test_generate_uuid_uniqueness():
    """
    Test that multiple generated UUIDs are unique.
    """
    # Generate multiple UUIDs
    uuids = [generate_uuid() for _ in range(1000)]
    
    # Check that all UUIDs are unique
    assert len(set(uuids)) == len(uuids), "Generated UUIDs should be unique"