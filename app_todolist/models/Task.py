from app_todolist.models import *


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.title