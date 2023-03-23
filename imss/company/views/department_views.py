from drf_spectacular.utils import extend_schema
from rest_framework.pagination import PageNumberPagination

from company.models.department import Department
from company.serializers.department_serializer import DepartmentSerializer
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_departments_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    departments = Department.objects.all()
    result_page = paginator.paginate_queryset(departments, request)
    serializer = DepartmentSerializer(result_page, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_detail_department(request, pk):
    department = Department.objects.get(id=pk)
    serializer = DepartmentSerializer(department, many=False)
    return Response(serializer.data)

@extend_schema(request=DepartmentSerializer())
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_department(request):
    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@extend_schema(request=DepartmentSerializer())
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def put_department(request, pk):
    department = Department.objects.get(id=pk)
    serializer = DepartmentSerializer(instance=department, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_department(request, pk):
    department = Department.objects.get(id=pk)
    department.active = False
    department.save()
    return Response("Item inativado com sucesso!")