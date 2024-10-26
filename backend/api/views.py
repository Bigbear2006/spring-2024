from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers
from jwt_auth.models import User


class BoardViewSet(ModelViewSet):
    serializer_class = serializers.BoardSerializer
    queryset = models.Board.objects.all()

    @action(["GET"], True, "search-tasks", "search-tasks")
    def search_tasks(self, request: Request, pk):
        query = request.GET.get("q")

        vector = SearchVector("title", weight="A") + SearchVector("description", weight="B")
        query = SearchQuery(query)
        rank = SearchRank(vector, query)

        board = self.get_object()
        tasks = board.tasks.annotate(search=vector, rank=rank).filter(search=query).order_by("-rank")
        data = serializers.TaskSerializer(tasks, many=True).data
        return Response(data, 200)

    @action(["GET"], True, "filter-tasks", "filter-tasks")
    def filter_tasks(self, request: Request, pk):
        responsible = request.GET.get("responsible")
        from_date = request.GET.get("from_date")
        to_date = request.GET.get("to_date")
        dates = request.GET.get("dates")

        tasks = self.get_object().tasks.all()
        if responsible is not None:
            vector = SearchVector("fio", weight="A")
            query = SearchQuery(responsible)
            users = User.objects.annotate(search=vector).filter(search=query)
            tasks = tasks.filter(responsible__in=users)

        if from_date is not None and to_date is not None:
            tasks = tasks.filter(created_at__range=(from_date, to_date))

        if dates is not None:
            tasks = tasks.filter(created_at__in=dates.split(','))

        data = serializers.TaskSerializer(tasks, many=True).data
        return Response(data, 200)


class TaskViewSet(ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Board.objects.all()
