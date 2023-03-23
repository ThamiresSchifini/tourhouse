from django import forms

from itmss.company.models.department import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['__all__']