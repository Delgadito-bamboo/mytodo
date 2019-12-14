from django.db import models
from django.utils import timezone
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Todo(models.Model):
    STATUS = (
        ('uncompleted','未完了'),
        ('completed','完了')
    )

    title = models.CharField(max_length=30)
    body = models.TextField(blank=True)
    due_date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    tag = models.ManyToManyField(Tag)
    status = models.CharField(max_length=30, choices=STATUS,default='uncompleted')

    def get_absolute_url(self):
        return reverse('todo_list')

    def __str__(self):
        return self.title


