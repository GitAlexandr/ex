from django.urls import path
from .views import ReportCreateView, ReportDetailView, ReportListView, ReportListAPIView, ReportDetailAPIView, ReportCreateAPIView


app_name = 'reports'


urlpatterns = [
    path('create/', ReportCreateView.as_view(), name='report_create'),
    path('list/', ReportListView.as_view(), name='report_list'),
    path('detail/<int:pk>/', ReportDetailView.as_view(), name='reports_detail'),
    path('api/create/', ReportCreateAPIView.as_view(), name='report_create_api'),
    path('api/list/', ReportListAPIView.as_view(), name='report_list_api'),
    path('api/detail/<int:pk>/', ReportDetailAPIView.as_view(), name='report_detail_api'),
]
