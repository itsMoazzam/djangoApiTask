from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskStatusUpdateView, TaskSummaryView

urlpatterns = [
    path('', TaskListCreateView.as_view(), name='tasks'),
    path('summary/', TaskSummaryView.as_view(), name='task-summary'),
    path('<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:pk>/status/', TaskStatusUpdateView.as_view(), name='task-status'),
]