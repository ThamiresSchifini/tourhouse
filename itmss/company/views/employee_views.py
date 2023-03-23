from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination

from company.filter_set.filter_sets import EmployeeFilterSet
from company.models.employee import Employee
from company.serializers.employee_serializer import EmployeeSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_employees_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    employees_filter = EmployeeFilterSet(request.GET, queryset=Employee.objects.all())
    filtered_queryset = employees_filter.qs
    result_page = paginator.paginate_queryset(filtered_queryset, request)
    serializer = EmployeeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_detail_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@extend_schema(request=EmployeeSerializer())
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




@extend_schema(request=EmployeeSerializer())
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def put_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer = EmployeeSerializer(instance=employee, data=request.data)
    if serializer.is_valid():
        departments = serializer.validated_data.pop('departments', None)  # remove os departments do validated_data
        if departments is not None:
            employee.departments.set(departments)  # adiciona os novos departments ao Employee
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.active = False
    employee.save()
    return Response("Item inativado com sucesso!")


