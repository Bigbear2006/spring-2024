from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from . import models, serializers


class BoardViewSet(ModelViewSet):
    serializer_class = serializers.BoardSerializer
    queryset = models.Board.objects.all()

    @action(["GET"], True, "search-tasks", "search-tasks")
    def search_tasks(self, request: Request):
        query = request.GET.get("q")

        vector = SearchVector("title", weight="A") + SearchVector("description", weight="B")
        query = SearchQuery(query)
        rank = SearchRank(vector, query)

        board = self.get_object()
        tasks = board.tasks.annotate(search=vector, rank=rank).filter(search=query).order_by("-rank")
        data = serializers.TaskSerializer(tasks, many=True).data
        return Response(data, 200)

    # @action(["GET"], True, "filter-tasks", "filter-tasks")
    # def filter_tasks(self, request: Request):
    #     responsible = request.GET.get("responsible")
    #     from_date = request.GET.get("from_date")
    #     to_date = request.GET.get("to_date")
    #     dates = request.GET.get("dates")
    #
    #     tasks = self.get_object().tasks.all()
    #     if responsible is not None:
    #         tasks.filter(responsible__in=responsible)


class TaskViewSet(ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()


class CommentViewSet(ModelViewSet):
    serializer_class = serializers.CommentSerializer
    queryset = models.Board.objects.all()
