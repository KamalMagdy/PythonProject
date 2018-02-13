from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from .forms import CategoryForm
from .models import Categories
from .forms import ForbiddenForm
from .models import ForbiddenWords
from .forms import PostForm
from .models import Posts
from .forms import TagForm
from .models import TagNames

from . import forms


def managerPanel(request):
    return render(request, "adminPanel/manager.html")

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
