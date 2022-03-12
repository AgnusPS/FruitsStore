from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from flask import request
from Home.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


# Create your views here.
def homepage(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method == "GET":
        return render(request,'register.html')
    else:
        obj = Customer.objects.all()                              
        name = request.POST.get("name")
        Cemail = request.POST.get("email")
        phno = request.POST.get("phno")
        place = request.POST.get("place")
        pswd = request.POST.get("pswd")
        cpswd = request.POST.get("cpswd")
        if pswd == cpswd:
            Customer.objects.create(customer_id = len(obj)+1 , customer_name = name,customer_email = Cemail,customer_phno = phno,customer_place = place,customer_password = pswd)
            User.objects.create_user(id = len(obj)+1, username = name, password = pswd, email=Cemail)
            send_mail(
                "message",
                "Haii "+name+" you are registered Successfully..!",
                settings.EMAIL_HOST_USER,
                [Cemail],
                fail_silently=False,
                
            )
            return render(request,"login.html")
        else:
            return HttpResponse("Password Doesn't Match")


def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    else:
        uname = request.POST.get("uname")
        pswd = request.POST.get("pswd")
        user = authenticate(username=uname, password=pswd)
        if user is not None:
            obj = Customer.objects.get(customer_name = uname)
            # return HttpResponse(obj.id)
            request.session["customerId"] = obj.id
            return redirect("Home:CustomerHome")
        else:
            return render(request,'login.html')

def CustomerHome(request):
    name = request.session.get("customerName")
    return render(request,"CustomerHome.html",{'obj':name})

def myprofile(request):
    cid = request.session.get("customerId")
    obj = Customer.objects.filter(id=cid)
    return render(request,"myprofile.html",{'obj':obj})

def editprofile(request):
    if request.method == 'GET':
        cid = request.session.get("customerId")
        obj = Customer.objects.filter(id=cid)
        return render(request,"editprofile.html",{'obj':obj.customer_name})
    else:
        name = request.session.get("customerName")
        obj = Customer.objects.filter(customer_name=name)
        Cname = request.POST.get("name")
        Cemail = request.POST.get("email")
        phno = request.POST.get("phno")
        place = request.POST.get("place")
        Customer.objects.filter(id=obj.id).update(customer_name = Cname)

      