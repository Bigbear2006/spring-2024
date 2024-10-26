from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class RegisterUserAPIView(CreateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()


class UserInfoAPIView(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
