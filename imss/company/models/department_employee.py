import uuid

from django.db import models
from django.db.models import CASCADE

from company.models.department import Department
from company.models.employee import Employee


class DepartmentEmployeeRelationType(models.TextChoices):
    CEO = ('CEO', 'CEO')
    DEV = ('DEV', 'Developer')
    MANAGER = ('MANAGER', 'Manager')


class DepartmentEmployee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=CASCADE)
    employee = models.ForeignKey(Employee, on_delete=CASCADE)
    relation_type = models.CharField(choices=DepartmentEmployeeRelationType.choices, max_length=100)