from rest_framework import serializers
from todos_app.models import TodosModel


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodosModel
        fields = ('id', 'title', 'description', 'status', 'creator', 'created_at')