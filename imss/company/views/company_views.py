from company.models.company import Company
from rest_framework.pagination import PageNumberPagination
from company.serializers.company_serializer import CompanySerializer
from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_companies_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    companies = Company.objects.all()
    result_page = paginator.paginate_queryset(companies, request)
    serializer = CompanySerializer(result_page, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_company_detail(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(company, many=False)
    return Response(serializer.data)


@extend_schema(request=CompanySerializer)
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def post_company(request):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@extend_schema(request=CompanySerializer)
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def put_company(request, pk):
    company = Company.objects.get(id=pk)
    serializer = CompanySerializer(instance=company, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def delete_company(request, pk):
    company = Company.objects.get(id=pk)
    company.active = False
    company.save()
    return Response("Item inativado com sucesso!")