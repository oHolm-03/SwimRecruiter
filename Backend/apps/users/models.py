# Custom user model with role field (athlete/coach)
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    Role_Choices = [('athlete', 'Athlete'), ('coach', 'Coach')]

    role = models.CharField(max_length=10, choices=Role_Choices)

    def __str__(self):
        return f"{self.username} ({self.role})"