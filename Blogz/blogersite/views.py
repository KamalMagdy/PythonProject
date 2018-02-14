from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from.forms import UserForm

def all_users(request):
    all_usr=User.objects.all()
    return  render(request,"all_users.html",{"all_usrs":all_usr})

def home(request):
    return render(request,"home.html")


def register(request):
    return render(request,"register.html")


def block(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.is_active=0
    us.save()
    all_usr = User.objects.all()
    return render(request,"all_users.html",{"all_usrs":all_usr})
    # return HttpResponseRedirect("allusers")

def unblock(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.is_active=1
    us.save()
    all_usr = User.objects.all()
    return render(request,"all_users.html",{"all_usrs":all_usr})
    # return HttpResponseRedirect("allusers")

def update(request,usr_id):
    usr=User.objects.get(id=usr_id)
    usr_form=UserForm(instance=usr)
    if request.method=="POST":
        usr_form=UserForm(request.POST,instance=usr)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("all_users.html")

    return render(request,"new.html",{"form":UserForm})



def delete(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.delete()

    all_usr = User.objects.all()
    return render(request,"all_users.html",{"all_usrs":all_usr})

def promote(request,usr_id):
    us = User.objects.get(id=usr_id)
    us.is_superuser=1
    us.save()
    all_usr = User.objects.all()
    return render(request, "all_users.html", {"all_usrs": all_usr})

def addnew(request):
    usr_form=UserForm()
    if request.method=="POST":
        usr_form=UserForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return  HttpResponseRedirect()
    return render(request,"new.html",{"form":usr_form})


def login_form(request):
    if request.method == 'POST':

        name = request.POST['username']
        password = request.POST['password']

        # authenticate first search for the user in database and if found
        # it returns user object
        # and if it didn't find a user it will return None
        user = authenticate(username=name, password=password)

        if user is not None:  # this means we found the user in database
            login(request, user)  # this means we put the user id in the session

            # return HttpResponse('logged in succes')
            return HttpResponseRedirect("home")
        else:
            return HttpResponseRedirect("register")
    return render(request, 'login_form.html')


# this is a decorator
# https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')

