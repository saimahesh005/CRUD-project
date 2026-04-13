from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
    template = loader.get_template('myfirsthtml.html')
    mymembers = Member.objects.all().values()
    context = { 'mymembers': mymembers }
    return HttpResponse(template.render(context, request))

def showrecords(request):
	template=loader.get_template('index.html')
	return HttpResponse( template.render() )

def index2(request):
	template=loader.get_template('index2.html')
	return HttpResponse( template.render() )

# using loader and HttpResponse functions.
def addrecords(request):
    fn=request.GET.get('text1')
    ln=request.GET.get('text2')
    member1=Member(firstname=fn, lastname=ln)
    member1.save()
    template=loader.get_template('myfirsthtml.html')
    mymembers1=Member.objects.all().values()
    context={'mymembers':mymembers1}
    return HttpResponse(template.render(context, request))

# using render function instead of loader and HttpResponse.
def updaterecords(request):
    id = request.GET.get('id')
    fn = request.GET.get('text1')
    ln = request.GET.get('text2')

    x = Member.objects.get(id=id)
    x.firstname = fn
    x.lastname = ln
    x.save()

    mymembers1 = Member.objects.all().values()
    context = {'mymembers': mymembers1}

    return render(request, 'myfirsthtml.html', context)
    
def deleterecords(request):
      id=request.GET.get('id')
      member1=Member.objects.get(id=id)
      member1.delete()
      template=loader.get_template('myfirsthtml.html')
      mymembers1=Member.objects.all().values()

      context={'mymembers':mymembers1}
      return render(request, 'myfirsthtml.html', context)
      




