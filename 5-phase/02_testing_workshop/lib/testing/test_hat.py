from lib.models.hat import Hat
from lib.models.user import User
import pytest

class TestHat:
    """Test the Hat Things"""

    def test_hat(self):
        """Hat has a user"""
        user = User()
        hat = Hat(type="cap", user=user)
        assert hat.user == user