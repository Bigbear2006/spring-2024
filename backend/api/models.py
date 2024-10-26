from django.db import models
from jwt_auth.models import User


class Board(models.Model):
    title = models.CharField(max_length=255)
    objects: models.Manager


class Task(models.Model):
    BACKLOG_STAGE = "backlog"
    IN_PROCESS_STAGE = "in process"
    COMPLETED_STAGE = "completed"
    stages = (
        (BACKLOG_STAGE, BACKLOG_STAGE),
        (IN_PROCESS_STAGE, IN_PROCESS_STAGE),
        (COMPLETED_STAGE, COMPLETED_STAGE),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    board = models.ForeignKey(Board, models.CASCADE, 'tasks')
    responsible = models.ForeignKey(User, models.SET_NULL, 'tasks', null=True)
    stage = models.CharField(max_length=50, choices=stages, default=BACKLOG_STAGE)
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)
    objects: models.Manager


class Comment(models.Model):
    task = models.ForeignKey(Task, models.CASCADE, 'comments')
    user = models.ForeignKey(User, models.CASCADE, 'comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects: models.Manager
