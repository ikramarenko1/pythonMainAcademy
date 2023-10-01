from django.contrib.auth.models import User
from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)  # blank=True - разрешает полю быть пустым
    createdate = models.DateTimeField(auto_now_add=True)
    completedate = models.DateTimeField(null=True, blank=True)
    isimportant = models.BooleanField(default=False)
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)  # on_delete=models.CASCADE - чтобы при удалении пользователя все записи, связанные с ним, удалялись

    def __str__(self):
        return self.title
