import json
from unittest import mock

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse

from itmss.models import User

from company.models.employee import Employee


class GetEmployeesListTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(
            email='user@email.com',
            username='testuser2',
            password='testpass'
        )
        self.company = {
            "cnpj": "string",
            "adress": "string",
            "city": "string",
            "country": "string",
            "active": True,
        }
        self.department = {
            "cost_center": "string",
            "name": "string",
            "integration_code": "string",
            "active": True,
            "company": 0
        }
        self.employee = Employee.objects.create(
           name="thamires",
           email="thamires@email.com",
           phone="33333333",
           birth="2000-01-01",
           entry="2020-01-01",
           shutdown=None,
           active=True,
           city="Florianópolis",
           departments=self.department,
           company=self.company.id
        )
        self.valid_payload = {
            "id": "ff1200ac-2234-448b-be2a-90c978f6dda3",
            "name": "thata",
            "email": "thata@email.com",
            "phone": "33333333",
            "birth": "2023-03-22",
            "entry": "2023-03-22",
            "shutdown": "2023-03-22",
            "active": True,
            "city": "Florianópolis",
            "departments": [],
            "companies": []
        }

        self.invalid_payload = {
            'name': "",
            'email': "thamires@email.com",
            'phone': "33333333",
            'birth': "2000-01-01",
            'entry': "2020-01-01",
            'shutdown': "",
            'active': True,
            'city': "Florianópolis",
            'departments': [{'cost_center': 'string', 'name': 'string',
                             'integration_code': 'string', 'active': True,
                             'company': 0}]}


    def test_get_employees_list(self):
        url = reverse('get-employees-list')
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('results' in response.data)
        self.assertTrue('count' in response.data)
        self.assertTrue('next' in response.data)
        self.assertTrue('previous' in response.data)
        self.assertEqual(len(response.data['results']), 1)

    @mock.patch('company.serializers.employee_serializer.EmployeeSerializer')
    def test_detail_employee(self, EmployeeSerializer):
        EmployeeSerializer.return_value = {}
        expected = self.employee.id
        url = reverse('get-detail-employee', args=[self.employee.pk])
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected)

    @mock.patch('company.serializers.employee_serializer.EmployeeSerializer')
    def test_post_valid_employee(self, EmployeeSerializer):
        EmployeeSerializer.return_value = ({})
        payload = json.dumps(self.valid_payload)
        response = self.client.post('/employees/create/', data=payload, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



