
from django.contrib import admin

from company.models.company import Company
from company.models.department import Department
from company.models.employee import Employee

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Company)
