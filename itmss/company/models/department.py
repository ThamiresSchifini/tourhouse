from django.db import models
from django.db.models import CASCADE

from company.models.company import Company


class Department(models.Model):
    cost_center = models.CharField(verbose_name='Centro de custo', null=False, blank=False, max_length=100)
    name = models.CharField(verbose_name='Nome', null=False, blank=False, max_length=100)
    integration_code = models.CharField(verbose_name='Código de integração', null=False, blank=False, max_length=100)
    active = models.BooleanField(verbose_name='Ativo', default=True)
    company = models.ForeignKey(Company, verbose_name='Empresa', on_delete=CASCADE)

    def __str__(self):
        return self.name
