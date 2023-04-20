from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from  django.core.files.storage import FileSystemStorage
from django.conf import settings
from . models import *




def index(request):
    return render(request,'index.html')

def indexx(request):
    return render(request,'index.html')

def register(request):
    return render(request,'userregister.html')

def addregister(request):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        email=request.POST.get('email')
        files=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(files.name,files)
        registration=userdetails(name=name,age=age,phone=phone,email=email,password=password,file=files)
        registration.save()
    return render(request,'userregister.html')

def addcontact(request):
    t=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        registration=usercontacts(name=name,phone=phone,email=email,usid=t)
        registration.save()
    return render(request,'addcontact.html')

def viewcontact(request):
    return render(request,'viewcontact.html')

def admin(request):
    return render(request,'adminprofile.html')

def user(request):
    return render(request,'userprofile.html')

def contactview(request):
    s=request.session['uid']
    a=usercontacts.objects.filter(usid=s)
    return render(request,'viewcontact.html',{'res':a})

def viewdetails(request):
    
    return render(request,'viewdetails.html')

def detailview(request):
    b=userdetails.objects.all()
    return render(request,'viewdetails.html',{'res':b})

def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return render(request, 'index.html')

    elif userdetails.objects.filter(email=email,password=password).exists():
        a=userdetails.objects.get(email=request.POST['email'], password=password)
        if a.password == request.POST['password']:
            request.session['uid'] = a.id
            request.session['uname'] = a.name

            request.session['email'] = email

            request.session['user'] = 'user'

            return render(request,'index.html')

    else:
        return render(request, 'login.html', {'status': 'Invalid email or Password'})

def userprofile(request):
    tem=request.session['uid']
    vpro=userdetails.objects.get(id=tem)
    return render(request,'userprofile.html',{'res' : vpro})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
     del request.session[key]
    return redirect(index)

def adminss(request):
    return render(request,'adminss.html')

def userinfo(request):
    b=userdetails.objects.all()
    return render(request,'adminss.html',{'res':b})

def delete(request,id):
    contacts=usercontacts.objects.get(id=id)
    contacts.delete()
    return redirect(contactview)

def deleteuser(request,id):
    users=userdetails.objects.get(id=id)
    users.delete()
    return redirect(userinfo)

def updateuser(request):
    return render(request,'updateuser.html')

def updatecontact(request):
    return render(request,'updatecontact.html')

def update(request,id):
    users=usercontacts.objects.get(id=id)
    return render(request,'updatecontact.html',{'res':users})

def updates(request,id):
    t=request.session['uid']
    if request.method=="POST":
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        registration=usercontacts(name=name,phone=phone,email=email,usid=t,id=id)
        registration.save()
        return redirect(contactview)

def update1(request,id):
    users=userdetails.objects.get(id=id)
    return render(request,'updateuser.html',{'res':users})

def updateuser(request,id):
    if request.method=="POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        email=request.POST.get('email')
        files=request.FILES['image']
        fs=FileSystemStorage()
        filename=fs.save(files.name,files)
        registration=userdetails(name=name,age=age,phone=phone,email=email,password=password,id=id,file=files)
        registration.save()
        return redirect(userprofile)

