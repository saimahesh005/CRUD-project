from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Employee

def members(request):
    template = loader.get_template('myfirsthtml.html')
    myemployees = Employee.objects.all().values()
    context = { 'myemployees': myemployees }
    return HttpResponse(template.render(context, request))



def home(request):
	template=loader.get_template('index.html')
	return HttpResponse( template.render() )

# using loader and HttpResponse functions.
def addrecords(request):
    fn=request.GET.get('text1')
    ln=request.GET.get('text2')
    email=request.GET.get('text3')
    phone=request.GET.get('text4')
    jobrole=request.GET.get('text5')
    salary=request.GET.get('text6')
    if fn and ln: 
        employee1 = Employee(
            firstname=fn,
            lastname=ln,
            email=email,
            phone=phone,
            jobrole=jobrole,
            salary=salary
        )
        employee1.save()
        return redirect('members')

# using render function instead of loader and HttpResponse.
def updaterecords(request):
    id = request.GET.get('id')
    
    try:
        x = Employee.objects.get(id=id)

        x.firstname = request.GET.get('text1')
        x.lastname = request.GET.get('text2')
        x.email = request.GET.get('text3')
        x.phone = request.GET.get('text4')
        x.jobrole = request.GET.get('text5')
        x.salary = request.GET.get('text6')

        x.save()

    except Employee.DoesNotExist:
        return HttpResponse("Employee not found")

    myemployees1 = Employee.objects.all().values()
    context = {'myemployees': myemployees1}

    return render(request, 'myfirsthtml.html', context)
    
def deleterecords(request):
    id=request.GET.get('id')
    try:
            x=Employee.objects.get(id=id)
            x.delete()
    except Employee.DoesNotExist:
         return HttpResponse("Employee not found")
    myemployees1=Employee.objects.all().values()
    context={'myemployees':myemployees1 }
    return render(request, 'myfirsthtml.html', context)   