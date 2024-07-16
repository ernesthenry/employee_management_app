# employees/urls.py

from django.urls import path
from .views import RegisterView, LoginView, EmployeeListCreateView, EmployeeDetailView, ExportEmployeeView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/export/', ExportEmployeeView.as_view(), name='employee-export'),
]
