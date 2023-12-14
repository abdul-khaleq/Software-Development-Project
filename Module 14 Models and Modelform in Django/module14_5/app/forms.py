from django import forms
from app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ['name','roll']
        # exclude = ['roll']
        labels ={
            'roll': 'Student Roll',
            'name': 'Student Name',
        }
        widgets ={
            'name': forms.TextInput(attrs={'class': 'btn btn-primary'}),
            # 'roll': forms.PasswordInput()
        }
        help_texts = {
            'name': 'Write your name:-'
        }
        error_messages ={
            'name': { 'required': 'Your name is required'}
        }