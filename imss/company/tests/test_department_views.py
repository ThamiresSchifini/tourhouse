from unittest import mock
from unittest.mock import patch

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from company.models.company import Company
from company.models.department import Department
from imss.models import User

class DepartmentTestCase(APITestCase):
    def setup(self):
        self.client = APIClient()

        self.company = Company.objects.create(cnpj='3333', adress='adress',
                                              city='Florianópolis', country='country',
                                              active=True)
        self.department = Department.objects.create(cost_center='3333', name='name',
                                              integration_code='Florianópolis',
                                              company=self.company, active=True)

        self.url_list = reverse('get-departments-list')
        self.url_detail = reverse('get-department-detail', args=[self.department.id])
        self.url_post = reverse('post-department')
        self.url_put = reverse('put-department', args=[self.department.id])
        self.url = reverse('delete-department', kwargs={'pk': self.department.pk})

        self.user = User.objects.create_user(
            email='user@email.com',
            username='testuser2',
            password='testpass'
        )

        self.data = {'id': 1, 'cost_center': '3333', 'name': 'name',
                     'integration_code': 'integration_code',
                     'company': self.company, 'active': True}

        self.valid_payload = {'cost_center': '12345678901234', 'name': 'T',
                              'integration_code': '3322', 'company': self.company, 'active': True}
        self.invalid_payload = {'cost_center': None, 'name': 'T',
                                'integration_code': '3322', 'company': self.company, 'active': True}

    #arrumar
    @mock.patch('company.serializers.department_serializer.DepartmentSerializer')
    def test_get_departments_list(self, DepartmentSerializer):
        mock_instance = DepartmentSerializer.return_value
        mock_instance.data = self.data
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0], mock_instance.data)

    @patch('company.serializers.department_serializer.DepartmentSerializer')
    def test_get_company_detail(self, mock_department_serializer):
        mock_serializer = mock_department_serializer.return_value
        mock_serializer.data = {
            'id': self.department.id,
            'cost_center': self.department.cost_center,
            'name': self.department.name,
            'integration_code': self.department.integration_code,
            'company': self.self.company,
            'active': self.department.active,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, mock_serializer.data)
