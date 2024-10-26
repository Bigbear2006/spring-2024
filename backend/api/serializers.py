from rest_framework.serializers import ModelSerializer

from . import models


class BoardSerializer(ModelSerializer):
    class Meta:
        model = models.Board
        fields = '__all__'


class TaskSerializer(ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super(CommentSerializer, self).create(validated_data)

    class Meta:
        model = models.Comment
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True}
        }
