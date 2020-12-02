from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    complete = models.BooleanField(default=False)
    def __str__(self):
        return self.task
