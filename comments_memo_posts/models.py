from django.db import models
from django.contrib.auth.models import User
from memo_posts.models import Memo


class MemoComment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    memo_post = models.ForeignKey(Memo, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_on']

        def __str__(self):
            return self.content
