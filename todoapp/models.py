from django.db import models
from django.conf import settings


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True)
    assignees = models.ManyToManyField(settings.AUTH_USER_MODEL)
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
