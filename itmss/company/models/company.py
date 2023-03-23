from django.db import models


class Company(models.Model):
    cnpj = models.CharField(verbose_name='Cnpj', blank=False, null=False, max_length=100)
    adress = models.CharField(verbose_name='Logradouro', blank=False, null=False, max_length=100)
    city = models.CharField(verbose_name='City', blank=False, null=False, max_length=100)
    country = models.CharField(verbose_name='País', blank=False, null=False, max_length=100)
    active = models.BooleanField(verbose_name='Ativo', default=True)

    def __str__(self):
        return self.cnpj
