from django.urls import path

from company.views.company_views import get_companies_list, get_company_detail, \
    post_company, put_company, delete_company

urlpatterns = [
    path('', get_companies_list, name='get-companies-list'),
    path('detail/<str:pk>/', get_company_detail, name='get-company-detail'),
    path('create/', post_company, name='post-company'),
    path('update/<str:pk>/', put_company, name='put-company'),
    path('delete/<str:pk>/', delete_company, name='delete-company'),
]