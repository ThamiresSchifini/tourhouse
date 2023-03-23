from unittest.mock import patch
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from company.models.company import Company
from itmss.models import User


class CompanyListTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()


        self.company = Company.objects.create(cnpj='3333', adress='adress',
                                              city='Florianópolis', country='country',
                                              active=True)
        self.url_list = reverse('get-companies-list')
        self.url_detail = reverse('get-company-detail', args=[self.company.id])
        self.url_post = reverse('post-company')
        self.url_put = reverse('put-company', args=[self.company.id])
        self.url = reverse('delete-company', kwargs={'pk': self.company.pk})

        self.user = User.objects.create_user(
            email='user@email.com',
            username='testuser2',
            password='testpass'
        )
        self.data = {'id': 1, 'cnpj': '3333', 'city': 'Florianópolis',
                'adress': 'adress', 'country': 'country', 'active': True}

        self.valid_payload = {'cnpj': '12345678901234', 'adress': 'Rua Teste, 123',
                              'city': 'Florianópolis', 'country': 'Brasil', 'active': True}
        self.invalid_payload = {'cnpj': None, 'adress': 'Rua Teste, 123',
                                'city': 'Florianópolis', 'country': 'Brasil', 'active': True}

    @patch('company.serializers.company_serializer.CompanySerializer')
    def test_get_companies_list(self, CompanySerializer):
        mock_instance = CompanySerializer.return_value
        mock_instance.data = self.data
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_list)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        self.assertEqual(response.data[0], mock_instance.data)

    @patch('company.serializers.company_serializer.CompanySerializer')
    def test_get_company_detail(self, mock_company_serializer):
        mock_serializer = mock_company_serializer.return_value
        mock_serializer.data = {
            'id': self.company.id,
            'cnpj': self.company.cnpj,
            'adress': self.company.adress,
            'city': self.company.city,
            'country': self.company.country,
            'active': self.company.active,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url_detail)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, mock_serializer.data)

    @patch('company.serializers.company_serializer.CompanySerializer')
    def test_post_company_with_valid_payload(self, mock_company_serializer):
        mock_serializer_instance = mock_company_serializer.return_value
        mock_serializer_instance.is_valid.return_value = True
        mock_serializer_instance.save.return_value = self.valid_payload

        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url_post, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['cnpj'], self.valid_payload['cnpj'])

    @patch('company.serializers.company_serializer.CompanySerializer')
    def test_valid_payload(self, mock_company_serializer):
        mock_instance = mock_company_serializer.return_value
        mock_instance.is_valid.return_value = True
        mock_instance.save.return_value = self.company

        self.client.force_authenticate(user=self.user)
        response = self.client.put(self.url_put, self.valid_payload, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_company(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, "Item inativado com sucesso!")

        company = Company.objects.get(pk=self.company.pk)
        self.assertFalse(company.active)
