from django.contrib.postgres.search import SearchRank, SearchQuery, SearchVector
from rest_framework.generics import RetrieveAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from . import models, serializers


class RegisterUserAPIView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class UserInfoAPIView(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class UsersListApiView(ListAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class UsersSearchListApiView(ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        query = self.request.GET.get("q")

        vector = SearchVector("username", weight="A") + SearchVector("fio", weight="A")
        query = SearchQuery(query, search_type="phrase")
        rank = SearchRank(vector, query)
        users = models.User.objects.annotate(search=vector, rank=rank).filter(search=query).order_by('-rank')
        return users
