from django.urls import path

from company.views.department_views import get_departments_list, get_detail_department, \
    post_department, put_department, delete_department

urlpatterns = [
    path('', get_departments_list, name='get-departments-list'),
    path('detail/<str:pk>/', get_detail_department, name='get-department-detail'),
    path('create/', post_department, name='post-department'),
    path('update/<str:pk>/', put_department, name='update-department'),
    path('delete/<str:pk>/', delete_department, name='delete-department'),
]