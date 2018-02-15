from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from.forms import UserForm, RegUserForm
from .forms import CategoryForm
from .models import Categories
from .forms import ForbiddenForm
from .models import ForbiddenWords
from .forms import PostForm
from .models import Posts
from .forms import TagForm
from .models import TagNames


def all_users(request):
    all_usr=User.objects.all()
    return  render(request,"adminPanel/all_users.html",{"all_usrs":all_usr})

def home(request):
    return render(request,"adminPanel/home.html")

def admin(request):
    return render(request,"adminPanel/Dashboard.html")


def register(request):
    return render(request,"adminPanel/register.html")


def block(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.is_active=0
    us.save()
    all_usr = User.objects.all()
    return render(request,"adminPanel/all_users.html",{"all_usrs":all_usr})
    # return HttpResponseRedirect("allusers")

def unblock(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.is_active=1
    us.save()
    all_usr = User.objects.all()
    return render(request,"adminPanel/all_users.html",{"all_usrs":all_usr})
    # return HttpResponseRedirect("allusers")

def update(request,usr_id):
    usr=User.objects.get(id=usr_id)
    usr_form=UserForm(instance=usr)
    if request.method=="POST":
        usr_form=UserForm(request.POST,instance=usr)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("/blogersite/allusers")

    return render(request,"adminPanel/new.html",{"form":usr_form})



def delete(request,usr_id):
    us=User.objects.get(id=usr_id)
    us.delete()

    all_usr = User.objects.all()
    return render(request,"adminPanel/all_users.html",{"all_usrs":all_usr})

def promote(request,usr_id):
    us = User.objects.get(id=usr_id)
    us.is_superuser=1
    us.save()
    all_usr = User.objects.all()
    return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})

def addnew(request):
    usr_form=UserForm()
    if request.method=="POST":
        usr_form=UserForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return  HttpResponseRedirect("/blogersite/allusers")
    return render(request,"adminPanel/new.html",{"form":usr_form})

def register(request):
    usr_form=RegUserForm()

    if request.method=="POST":
        usr_form=RegUserForm(request.POST)
        if usr_form.is_valid():
            usr_form.save()
            return HttpResponseRedirect("/blogersite/home")
    return render(request, "adminPanel/register.html",{"form":usr_form})

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
            return HttpResponseRedirect("/blogersite/home")
        else:
            return HttpResponseRedirect("/blogersite/register")
    return render(request, 'adminPanel/login_form.html')


# this is a decorator
# https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')




def managerPanel(request):
    return render(request, "adminPanel/Dashboard.html")

def allCategories(request):
    all_categories = Categories.objects.all()
    context = {"allCategories": all_categories}
    return render(request, "adminPanel/all_cat.html", context)


def getCategory(request, cat_id):
    get_category = Categories.objects.get(id=cat_id)
    context = {"allCategories": get_category}
    return render(request, "adminPanel/cat_details.html", context)


def newCategory(request):
    category_form = CategoryForm()
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect('/blogersite/allCategories/')
    context = {"form": category_form}
    return render(request, 'adminPanel/new_cat.html', context)


def category_delete(request, cat_id):
    obj = Categories.objects.get(id=cat_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allCategories/')


def category_edit(request, cat_id):
    category = Categories.objects.get(id=cat_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blogersite/allCategories/')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'adminPanel/edit_cat.html', {'form': form})

#######################################
#ForbideentWords

def allForbidden(request):
    all_forbidden = ForbiddenWords.objects.all()
    context = {"allForbidden": all_forbidden}
    return render(request, "adminPanel/all_forbid.html", context)


# def getForbidden(request, forbid_id):
#     get_category = Categories.objects.get(id=forbid_id)
#     context = {"allCategories": get_category}
#     return render(request, "adminPanel/cat_details.html", context)


def newForbidden(request):
    forbidden_form = ForbiddenForm()
    if request.method == "POST":
        forbidden_form = ForbiddenForm(request.POST)
        if forbidden_form.is_valid():
            forbidden_form.save()
            return HttpResponseRedirect('/blogersite/allForbidden/')
    context = {"form": forbidden_form}
    return render(request, 'adminPanel/new_forbid.html', context)


def forbidden_delete(request, forbidden_id):
    obj = ForbiddenWords.objects.get(id=forbidden_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allForbidden/')


def forbidden_edit(request, forbidden_id):
    forbid = ForbiddenWords.objects.get(id=forbidden_id)

    if request.method == "POST":
        form = ForbiddenForm(request.POST, instance=forbid)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blogersite/allForbidden/')
    else:
        form = ForbiddenForm(instance=forbid)
    return render(request, 'adminPanel/edit_forbid.html', {'form': form})


####################################################
#Tag Names
####################################################
def allTags(request):
    all_tag = TagNames.objects.all()
    context = {"allTags": all_tag}
    return render(request, "adminPanel/all_tag.html", context)


def newTag(request):
    tag_form = TagForm()
    if request.method == "POST":
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect('/blogersite/allTags/')
    context = {"form": tag_form}
    return render(request, 'adminPanel/new_tag.html', context)


def tag_delete(request, tag_id):
    obj = TagNames.objects.get(id=tag_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allTags/')


def tag_edit(request, tag_id):
    tag = TagNames.objects.get(id=tag_id)

    if request.method == "POST":
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blogersite/allTags/')
    else:
        form = TagForm(instance=tag)
    return render(request, 'adminPanel/edit_tag.html', {'form': form})

####################################################
#Posts
####################################################

def allPosts(request):
    all_posts = Posts.objects.all()
    context = {"allPosts": all_posts}
    return render(request, "adminPanel/all_post.html", context)


def getPosts(request, post_id):
    get_posts = Posts.objects.get(id=post_id)
    context = {"allPosts": get_posts}
    return render(request, "adminPanel/post_details.html", context)


def newPost(request):
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            #post_form.post_image = request.FILES['post_image']
            post_form.save()
            return HttpResponseRedirect('/blogersite/allPosts/')
    context = {"form": post_form}
    return render(request, 'adminPanel/new_post.html', context)


def post_delete(request, post_id):
    obj = Posts.objects.get(id=post_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allPosts/')


def post_edit(request, post_id):
    post = Posts.objects.get(id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blogersite/allPosts/')
    else:
        form = PostForm(instance=post)
    return render(request, 'adminPanel/edit_post.html', {'form': form})
