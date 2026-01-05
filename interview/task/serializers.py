from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Task
        fields = ('id','title','description','owner','created_at', 'status')
        read_only_fields = ('id','owner','created_at')

    def create(self, validated_data):
        # owner will be set in view.perform_create
        return Task.objects.create(**validated_data)


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('status',)

    def validate_status(self, value):
        # ensure the status is one of the model's choices
        valid = [choice[0] for choice in Task.STATUS_CHOICES]
        if value not in valid:
            raise serializers.ValidationError('Invalid status')
        return value