from django import forms
from .models import Student, Admission

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class AdmissionForm(forms.ModelForm):
    class Meta:
        model = Admission
        fields = '__all__'
