from django import forms
from empmngt.models import Employee, Calender, News, Job
from django.contrib.auth.models import User

class CalenderForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = '__all__'
        
        widgets = {
            'Date': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type':'date',
                'placeholder': 'Date of Joining',
            }),

            'Occasion': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Occasion',
                'rows': 4
            }),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            'Name': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter your name'
            }),

            'Emp_ID': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Employee ID'
            }),

            'Designation': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Designation'
            }),

            'Date_of_Joining': forms.DateInput(attrs={
                'class': 'form-control w-100',
                'type':'date',
                'placeholder': 'Date of Joining',
            }),
            
            'Department': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Department'
            }),

            'Annual_CTC': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Annual CTC'
            }),

            'Experience': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Experience'
            }),
        }
        
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        
        widgets = {
            'Details': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Details',
                'rows': 4
            }),
        }

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
        
        widgets = {
            'Role': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Role'
            }),

            'Experience': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Experience'
            }),

            'Skills': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Skills'
            }),
            
            'CTC': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter CTC'
            }),

            'Notice_Period': forms.TextInput(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Notice Period'
            }),
        }
 