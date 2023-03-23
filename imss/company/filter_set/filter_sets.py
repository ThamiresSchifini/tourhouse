from company.models.employee import Employee
from django_filters import rest_framework as filters

class EmployeeFilterSet(filters.FilterSet):
    city = filters.CharFilter(lookup_expr='icontains')
    departments = filters.CharFilter(lookup_expr='icontains')
    company = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Employee
        fields = ['city', 'departments', 'company']