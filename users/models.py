from django.contrib.auth.models import User
from django.db import models
import random

class ConfirmationCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = ''.join(random.choices('0123456789', k=6))
        super().save(*args, **kwargs)

