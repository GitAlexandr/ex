from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from .forms import ReportForm
from .models import Report
from django.urls import reverse_lazy

class ReportCreateView(LoginRequiredMixin, CreateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/reports_create.html'
    success_url = reverse_lazy('reports:report_list')

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ReportListView(ListView):
    model = Report
    template_name = 'reports/report_list.html'
    context_object_name = 'reports'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/reports_detail.html'

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Report
from .serializers import ReportSerializer

class ReportCreateAPIView(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
    

class ReportListAPIView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

class ReportDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]
