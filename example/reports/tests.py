from django.test import TestCase
from .models import Report
from django.contrib.auth.models import User
from .forms import ReportForm
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from rest_framework import status


class ReportModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='dsdsadasd')
        Report.objects.create(title='Test Report', user=test_user, car_number='12345', description='Test description', status='new')

    def test_title_content(self):
        report = Report.objects.get(id=1)
        expected_object_name = f"{report.title} #1 - {report.car_number}"
        self.assertEqual(expected_object_name, str(report))


class ReportFormTest(TestCase):
    def test_report_form_valid(self):
        test_user = User.objects.create_user(username='testuser', password='dsdsadasd')
        form_data = {'title': 'Test Report', 'user': test_user.id, 'car_number': '12345', 'description': 'Test description', 'status': 'new'}
        form = ReportForm(data=form_data)
        self.assertTrue(form.is_valid())


class ReportListView(LoginRequiredMixin, ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'
    paginate_by = 10

    def get_queryset(self):
        return Report.objects.filter(user=self.request.user).order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = True
        return context



class ReportAPITest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = User.objects.create_user(username='testuser', email='test@example.com', password='dsadsaddsa')
        Report.objects.create(title='Test Report', user=cls.test_user, car_number='12345', description='Test description', status='new')

    def test_get_report_list(self):
        self.client.login(username=self.test_user.username, password='dsadsaddsa')
        url = '/reports/api/list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)

    def test_create_report(self):
        self.client.login(username=self.test_user.username, password='dsadsaddsa')
        url = '/reports/api/create/'
        data = {'title': 'New Report', 'user': self.test_user.id, 'car_number': '67890', 'description': 'New description', 'status': 'new'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)