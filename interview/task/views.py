from rest_framework import generics, permissions
from rest_framework.permissions import BasePermission
from .models import Task
from .serializers import TaskSerializer, TaskStatusSerializer

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Debug prints to inspect incoming auth headers and user resolution
        auth_header = self.request.headers.get('Authorization')
        print('DEBUG: Authorization header ->', auth_header)
        print('DEBUG: request.user ->', self.request.user, 'authenticated:', getattr(self.request.user, 'is_authenticated', False))
        user = self.request.user
        # return only tasks that belong to the authenticated user
        return Task.objects.filter(owner__email=user.email)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    lookup_field = 'pk'


class TaskStatusUpdateView(generics.UpdateAPIView):
    """Endpoint to update only the status of a task. Only owner may change status."""
    serializer_class = TaskStatusSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    queryset = Task.objects.all()
    lookup_field = 'pk'


from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

class TaskSummaryView(APIView):
    """Return a summary (counts per status) for the authenticated user's tasks."""
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        qs = Task.objects.filter(owner=request.user)
        counts = qs.values('status').annotate(count=Count('id'))
        data = {choice[0]: 0 for choice in Task.STATUS_CHOICES}
        total = 0
        for item in counts:
            data[item['status']] = item['count']
            total += item['count']
        data['total'] = total
        return Response(data)
