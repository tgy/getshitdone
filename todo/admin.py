from django.contrib import admin
from todo import models

admin.site.register(models.Board)
admin.site.register(models.Task)
