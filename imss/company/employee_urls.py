from django.urls import path

from company.views.employee_views import get_employees_list, get_detail_employee, post_employee, put_employee, delete_employee

urlpatterns = [
    path('', get_employees_list, name='get-employees-list'),
    path('detail/<str:pk>/', get_detail_employee, name='get-detail-employee'),
    path('create/', post_employee, name='post-employee'),
    path('update/<str:pk>/', put_employee, name='put-employee'),
    path('delete/<str:pk>/', delete_employee, name='delete-employee'),
]
