from django.db import models
from django.contrib.auth.models import AbstractUser

USER_ROLES = (
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('admin', 'Admin'),
)

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=USER_ROLES, default='student')
    mobile = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"