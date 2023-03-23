from rest_framework import serializers

from company.models.employee import Employee
from company.serializers.department_serializer import DepartmentSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, allow_null=False)

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'phone', 'birth', 'entry', 'shutdown',
                  'active', 'city', 'departments', 'companies')
