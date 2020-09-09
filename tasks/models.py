from django.db import models


class TasksDB(models.Model):
    content = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)
