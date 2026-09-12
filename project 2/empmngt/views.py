from django.shortcuts import render, redirect
from empmngt.models import Calender, Employee, News, Job
from empmngt.forms import CalenderForm, EmployeeForm, NewsForm, JobForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponse
import csv

# Create your views here.

def home(request):
    return render(request, 'empmngt/home.html')

def addnews(request):
    f=NewsForm()
    if request.method == 'POST':
        f = NewsForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/news')
    return render(request, 'empmngt/addnews.html',  {'form':f})

def calender(request):
    f=CalenderForm()
    if request.method == 'POST':
        f = CalenderForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/holidays')
    return render(request, 'empmngt/calender.html',  {'form':f})

def viewemp(request):
    data = Employee.objects.all()
    return render(request, 'empmngt/viewemp.html', {'d': data})

def holidays(request):
    data = Calender.objects.all()
    return render(request, 'empmngt/holidays.html', {'d': data})

def news(request):
    data = News.objects.last()
    return render(request, 'empmngt/news.html', {'d': data})

def employee(request):
    f=EmployeeForm()
    if request.method == 'POST':
        f = EmployeeForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/viewemp')
    return render(request, 'empmngt/addemp.html', {'form':f})

@login_required
def dashboardview(request):
    return render(request, 'empmngt/dashboard.html')

def empdashboard(request):
    return render(request, 'empmngt/empdash.html')

def loginview(request):
    return render(request, 'registration/login.html')

def logoutview(request):
    logout(request)
    return redirect('/login')

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename="employeelist.csv"'
    employee = Employee.objects.all()
    writer = csv.writer(response)
    writer.writerow(['Name', 'Emp ID', 'Designation','Department', 'Annual CTC', 'Experience'])
    for emp in employee:
        writer.writerow([emp.Name, emp.Emp_ID, emp.Designation, emp.Department, emp.Annual_CTC, emp.Experience])
    return response

def updateview(request, id):
    data = Employee.objects.get(id=id)
    f = EmployeeForm(request.POST, instance=data)
    if f.is_valid():
        f.save()
        return redirect('/viewemp')
    return render(request, 'empmngt/empupdate.html', {'d': data})

def newsupdate(request, id):
    data = News.objects.get(id=id)
    f = NewsForm(request.POST, instance=data)
    if f.is_valid():
        f.save()
        return redirect('/news')
    return render(request, 'empmngt/newsupdate.html', {'d': data})

def newsdelete(request, id):
    data = News.objects.get(id=id)
    data.delete()
    return redirect('/')

def deleteview(request, id):
    data = Employee.objects.get(id=id)
    data.delete()
    return redirect('/viewemp')

def jobopen(request):
    f=JobForm()
    if request.method == 'POST':
        f = JobForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('/jobs')
    return render(request, 'empmngt/jobopen.html',  {'form':f})

def jobs(request):
    data = Job.objects.all()
    return render(request, 'empmngt/jobs.html', {'d': data})
