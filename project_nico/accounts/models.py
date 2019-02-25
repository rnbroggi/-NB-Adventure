from django.contrib.auth import models as auth_models
from django.db import models


# Built in Django User model
class User(auth_models.User, auth_models.PermissionsMixin):

    def __str__(self):
        return self.username
