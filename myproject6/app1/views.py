from django.shortcuts import render
from django.http import HttpResponse
from app1.models import emplyee
import faker

fake = faker.Faker()

def faker_view(request):
    for i in range(1000):
        first_name = fake.first_name()
        last_name = fake.last_name()
        job = fake.random_element(elements=('Software', 'Admin', 'Web Developer', 'IT', 'Govt', 'Trainer'))
        email = fake.email()
        salary = fake.random_element(elements=(40000, 50000, 60000, 80000, 20000, 400000))
        city = fake.random_element(elements=('hyderabaad', 'bangluru', 'mumbai', 'indour','pune', 'chennai'))
        state = fake.state()
        address = fake.address()

        data = emplyee(
            first_name=first_name,
            last_name=last_name,
            job=job,
            email=email,
            salary=salary,
            city=city,
            state=state,
            address=address
        )
        data.save()

    context = emplyee.objects.all()
    total_emp = len(context)

    return render(request, 'fakerdata.html',{'emp' : context , 'total_emp' : total_emp} )


def index_page(request):
    return render(request, 'index.html')


def hyddata(request):
    if request.method=='POST':
        job1=request.POST.get('job1')
        context=emplyee.objects.filter(city='hyderabaad') & emplyee.objects.filter(job=job1)
        total = len(context)
        return render(request, 'hyderabaad_data.html', {'emp': context, 'total_emp': total})

    else:
       context = emplyee.objects.filter(city='hyderabaad')

       total = len(context)
       return render(request, 'hyderabaad_data.html',{'emp' : context ,'total_emp' : total})


def bangluru(request):
    if request.method=='POST':
        job1 = request.POST.get('job1')
        context = emplyee.objects.filter(city='bangluru') & emplyee.objects.filter(job=job1)
        total = len(context)
        return render(request, 'banglor_data.html', {'emp' : context , 'total_emp' : total})

    else:

        context = emplyee.objects.filter(city='bangluru')
        total = len(context)
        return render(request, 'banglor_data.html', {'emp' : context , 'total_emp' : total})


def chennai(request):
    if request.method=='POST':
        job1=request.POST.get('job1')
        context = emplyee.objects.filter(city='chennai') & emplyee.objects.filter(job=job1)
        total = len(context)
        return render(request,'chennai_data.html',{'emp' : context , 'total_emp' : total})

    else:
        context = emplyee.objects.filter(city='chennai')
        total = len(context)
        return render(request, 'chennai_data.html',{'emp' : context , 'total_emp' : total})


def pune(request):
    if request.method=='POST':
        job1 = request.POST.get('job1')
        context = emplyee.objects.filter(city='indour') & emplyee.objects.filter(job=job1)

        total = len(context)
        return render(request,'pune_data.html',{'emp' : context , 'total_emp' : total})
    else:
        context = emplyee.objects.filter(city='indour')
        total = len(context)

        return render(request, 'pune_data.html',{'emp' : context , 'total_emp' : total})
