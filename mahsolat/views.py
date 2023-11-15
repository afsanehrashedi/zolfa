from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import kala
# Create your views here.
def home(request):
  return render(request,"mahsolat/index.html")

def arayeshi(request):
    l=kala.objects.all()
    return render(request,"mahsolat/arayeshi.html",context={"kalaha":l})



def error(request):
  return render(request,"mahsolat/error.html")


def sc(request):
  return render(request,"mahsolat/sc.html")


def reg(request):
  if request.method=="POST":
    status=False
    context={'errors':[]}
    f=request.POST.get("fname")
    l=request.POST.get("lname")
    e=request.POST.get("email")
    u=request.POST.get("username")
    p=request.POST.get("password")
    rp=request.POST.get("repassword")
    if len(p)<6:
      status=True
      context['errors'].append("password must be 6 characters")
    if (p!=rp):
      status=True
      context['errors'].append("re-password is not match")
    if (status==False):
      User.objects.create(username=u,password=p,email=e)
      return redirect("/success")
    else:
       return render(request,"mahsolat/reg.html",context=context)

  return render(request,"mahsolat/reg.html")
def upanel(request):
  if request.user.is_authenticated:
    return render(request,"mahsolat/upanel.html")
  else:
    return render(request,"mahsolat/users.html")  

def behdashti(request):
  return render(request,"mahsolat/behdashti.html")





def lout(request):
  logout(request)
  return redirect("/")

def users(request):
  if(request.method=="post"):
    u=request.POST.get("username")
    p=request.POST.get("password")
    user=authenticate(request,username=u,password=p)
    if user is not None:
      login(request,user)
      return redirect("/upanel")
    else:
      return redirect("/error")

  return render(request,"mahsolat/users.html")

def contact(request):
  return render(request,"mahsolat/contact.html")