from django import forms

from imss.company.models.department import Department


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['__all__']