from django.db import models
from django.contrib.auth.models import User

class NotifyUser(User):
    class Meta:
        managed = False