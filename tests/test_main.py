import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from main import generate_password, check_strength, generate_many


def test_length():
    assert len(generate_password(16)) == 16


def test_many():
    assert len(generate_many(5)) == 5


def test_strength():
    assert check_strength("abc") == "Очень слабый"
