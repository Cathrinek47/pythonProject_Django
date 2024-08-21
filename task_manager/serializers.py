from rest_framework import serializers
from .models import *
# from .validators import *


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', "deadline"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()

    class Meta:
        model = Task
        fields = '__all__'

