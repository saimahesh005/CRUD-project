from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee


# Display all employees
def members(request):
    myemployees = Employee.objects.all()
    return render(request, 'myfirsthtml.html', {'myemployees': myemployees})


# Home page
def home(request):
    return render(request, 'index.html')


# ADD RECORD (POST)
def addrecords(request):
    if request.method == "POST":
        fn = request.POST.get('text1')
        ln = request.POST.get('text2')
        email = request.POST.get('text3')
        phone = request.POST.get('text4')
        jobrole = request.POST.get('text5')
        salary = request.POST.get('text6')

        if fn and ln:
            Employee.objects.create(
                firstname=fn,
                lastname=ln,
                email=email,
                phone=phone,
                jobrole=jobrole,
                salary=salary
            )
        return redirect('members')


# UPDATE RECORD (POST)
def updaterecords(request):
    if request.method == "POST":
        id = request.POST.get('id')

        try:
            x = Employee.objects.get(id=id)

            x.firstname = request.POST.get('text1')
            x.lastname = request.POST.get('text2')
            x.email = request.POST.get('text3')
            x.phone = request.POST.get('text4')
            x.jobrole = request.POST.get('text5')
            x.salary = request.POST.get('text6')

            x.save()

        except Employee.DoesNotExist:
            return HttpResponse("Employee not found")

        return redirect('members')


# DELETE RECORD (POST)
def deleterecords(request):
    if request.method == "POST":
        id = request.POST.get('id')

        try:
            x = Employee.objects.get(id=id)
            x.delete()
        except Employee.DoesNotExist:
            return HttpResponse("Employee not found")

        return redirect('members')