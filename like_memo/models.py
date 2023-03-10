from django.db import models
from django.contrib.auth.models import User
from memo_posts.models import Memo


class MemoLikes(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    memo_post = models.ForeignKey(
        Memo, related_name='like_memo', on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'memo_post']

    def __str__(self):
        return f'{self.owner} {self.memo_post}'
