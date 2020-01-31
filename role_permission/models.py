from django.db import models

# Create your models here.

class Permission(models.Model):
    name = models.CharField(max_length=50, help_text='Permission name')

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, help_text='Role name')
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name