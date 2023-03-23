import enum
import uuid

from django.db import models

from company.models.department import Department


class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Nome', blank=False, null=False, max_length=100)
    email = models.CharField(verbose_name='Email', blank=False, null=False, max_length=100)
    phone = models.CharField(verbose_name='Telefone', blank=False, null=False, max_length=100)
    birth = models.DateField(verbose_name="Data de nascimento", blank=False, null=False)
    entry = models.DateField(verbose_name='Data de entrada', blank=False, null=False)
    shutdown = models.DateField(verbose_name='Data de desligamento', blank=True, null=True)
    active = models.BooleanField(verbose_name='Ativo', default=True)
    city = models.CharField(verbose_name='Cidade', blank=False, null=False, max_length=100)
    departments = models.ManyToManyField(Department, related_name='employees', through='DepartmentEmployee')

    def __str__(self):
        return self.name

    @property
    def companies(self):
        return self.departments.values_list('company')
