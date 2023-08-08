from datetime import timezone
import uuid

from django.contrib.auth import get_user_model

from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.amount}"

class Income(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return f"{self.amount}"
