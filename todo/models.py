from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from todo import status

class Board(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50, blank=True)
    color = models.CharField(max_length=7, choices=status.BOARD_COLORS,
                             default=status.BLUE)

    creation_date = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Task(models.Model):

    board = models.ForeignKey(Board, blank=True, db_index=True)
    text = models.TextField()
    assignee = models.ForeignKey(User, blank=True, null=True)
    status = models.CharField(max_length=20, choices=status.TASK_STATUSES,
                              default=status.WISH)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)

    def status_verbose(self):
        return dict(status.TASK_STATUSES)[self.status]

    def __str__(self):
        return self.text
