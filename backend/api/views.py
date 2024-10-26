from rest_framework.viewsets import ModelViewSet

from . import models, serializers


class BoardViewSet(ModelViewSet):
    serializer_class = serializers.BoardSerializer
    queryset = models.Board.objects.all()


class TaskViewSet(ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Board.objects.all()
