from lib.models.user import User
import pytest

class TestUser:
    """Test the User =>"""
    def test_user_init(self):
        """Can create a user instance"""
        user = User()
        assert user.username == ""

    def test_user_has_username(self):
        """User has a username"""
        user = User(username="Carla")
        assert user.username == "Carla"