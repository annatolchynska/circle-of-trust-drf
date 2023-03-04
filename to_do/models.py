from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    task_title = models.CharField(max_length=250)
    content = models.TextField()
    due_date = models.DateField(null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.task_title}'
