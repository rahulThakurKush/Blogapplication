from datetime import datetime
from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserModel(AbstractUser):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255,unique=True)
    password = models.CharField(max_length=255)
    otp = models.CharField(max_length=6)
    otp_send_time = models.DateTimeField(default=timezone.now)
    is_varified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

