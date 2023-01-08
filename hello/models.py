from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=155)
    second_name = models.CharField(max_length=155)
    email = models.EmailField()

    def __str__(self):
        return self.first_name





