from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from .models import Task

User = get_user_model()

class TaskSummaryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user1 = User.objects.create_user(email='u1@example.com', password='secret123')
        self.user2 = User.objects.create_user(email='u2@example.com', password='secret123')
        # create tasks for user1
        Task.objects.create(title='t1', owner=self.user1, status=Task.STATUS_PENDING)
        Task.objects.create(title='t2', owner=self.user1, status=Task.STATUS_IN_PROGRESS)
        Task.objects.create(title='t3', owner=self.user1, status=Task.STATUS_COMPLETED)
        # user2 tasks
        Task.objects.create(title='u2t1', owner=self.user2, status=Task.STATUS_PENDING)

    def test_summary_counts_user1(self):
        self.client.force_authenticate(self.user1)
        resp = self.client.get(reverse('task-summary'))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['pending'], 1)
        self.assertEqual(data['in_progress'], 1)
        self.assertEqual(data['completed'], 1)
        self.assertEqual(data['total'], 3)

    def test_summary_counts_user2(self):
        self.client.force_authenticate(self.user2)
        resp = self.client.get(reverse('task-summary'))
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data['pending'], 1)
        self.assertEqual(data['in_progress'], 0)
        self.assertEqual(data['completed'], 0)
        self.assertEqual(data['total'], 1)
