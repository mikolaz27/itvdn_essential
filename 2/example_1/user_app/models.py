from django.db import models

from django.contrib.auth.models import User
from user_app.managers import PersonManager


class Person(User):
    people = PersonManager()

    class Meta:
        proxy = True
        ordering = ('first_name',)

    def do_something(self):
        print(self.username)
