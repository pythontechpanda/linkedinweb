from django.db import models
from accounts.models import User


class Message(models.Model):
    author=models.ForeignKey(User, related_name='author_messages', on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.author.first_name

    def last_30_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]