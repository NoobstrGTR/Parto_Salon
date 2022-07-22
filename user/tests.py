
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""
    
    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            '09186550945',
            'test123',
        )
        
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)