from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as django_logout
from django.contrib.auth.models import User
from .forms import  *
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def home(request):
    subcat = sub(request)
    post_list = Posts.objects.all().order_by('-post_date')
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {'allCategories': Categories.objects.all(), 'allPosts': posts, "subcat": subcat}
    return render(request, "hometemp/home.html", context)


#######################################
#                Users                #
#######################################
@login_required
def all_users(request):
    if request.user.is_superuser:
        all_usr = User.objects.all()
        return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})
    else:
        return render(request, "hometemp/notallowed")

# @login_required(login_url='adminPanel/login_form')
# @login_required
def admin(request):
    if request.user.is_superuser:
        return render(request, "adminPanel/Dashboard.html")
    else:
        return render(request,"hometemp/notallowed")
@login_required
def block(request, usr_id):
    if request.user.is_superuser:
        us = User.objects.get(id=usr_id)
        us.is_active = 0
        us.save()
        all_usr = User.objects.all()
        return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})
    else:
        return render(request,"hometemp/notallowed")

@login_required
def unblock(request, usr_id):
    if request.user.is_superuser:
        us = User.objects.get(id=usr_id)
        us.is_active = 1
        us.save()
        all_usr = User.objects.all()
        return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})
    else:
        return render(request,"hometemp/notallowed")

@login_required
def update(request, usr_id):
    if request.user.is_superuser:
        usr = User.objects.get(id=usr_id)
        usr_form = RegUserForm(instance=usr)
        if request.method == "POST":
            usr_form = RegUserForm(request.POST, instance=usr)
            if usr_form.is_valid():
                usr_form.save()
                return HttpResponseRedirect("/blogersite/allusers/")

        return render(request, "adminPanel/new.html", {"form": usr_form})
    else:
        return render(request, "hometemp/notallowed")

@login_required
def delete(request, usr_id):
    if request.user.is_superuser:
        us = User.objects.get(id=usr_id)
        us.delete()
        all_usr = User.objects.all()
        return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})
    else:
        return render(request, "hometemp/notallowed")


@login_required
def promote(request, usr_id):
    if request.user.is_superuser:
        us = User.objects.get(id=usr_id)
        us.is_superuser = 1
        us.save()
        all_usr = User.objects.all()
        return render(request, "adminPanel/all_users.html", {"all_usrs": all_usr})
    else:
        return render(request, "hometemp/notallowed")


@login_required
def addnew(request):
    if request.user.is_superuser:
        usr_form = RegUserForm()
        if request.method == "POST":
            usr_form = RegUserForm(request.POST)
            if usr_form.is_valid():
                usr_form.save()
                return HttpResponseRedirect("/blogersite/allusers/")
        return render(request, "adminPanel/new.html", {"form": usr_form})
    else:
        return render(request, "hometemp/notallowed")


def register(request):
    usr_form=RegUserForm()

    if request.method=="POST":
        usr_form=RegUserForm(request.POST)
        if usr_form.is_valid():
            usermail = User.objects.filter(email=request.POST['email'])
            if usermail.exists():
                return render(request, "adminPanel/register.html", {"form": usr_form, "repeatedmail": 1})
            usr_form.save()
            reg_username = request.POST['username']
            reg_password = request.POST['password1']
            user = authenticate(username=reg_username, password=reg_password)
            login(request, user)
            return HttpResponseRedirect("/blogersite/home")
    return render(request, "adminPanel/register.html",{"form":usr_form})

#######################################
#           Authentications           #
#######################################

@login_required
def logout(request):
    django_logout(request)
    logout(request)
    return HttpResponseRedirect("/blogersite/home")


def login_form(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        if user:
            if user.is_active == 0:
                return render(request, 'adminPanel/login_form.html',{"block":1})

        if user is not None:  # this means we found the user in database
            login(request, user)  # this means we put the user id in the session
            return HttpResponseRedirect("/blogersite/home")
        else:
            return render(request,"adminPanel/login_form.html",{"openreg":1})
    return render(request, 'adminPanel/login_form.html')

# https://docs.djangoproject.com/en/2.0/topics/auth/default/#the-login-required-decorator
@login_required
def logged_in_only(request):
    return HttpResponse('you are authenticated')


#######################################
# Categories                          #
#######################################
def allCategories(request):
    all_categories = Categories.objects.all()
    context = {"allCategories": all_categories}
    return render(request, "adminPanel/all_cat.html", context)


def getCategory(request,cat_id):
    get_category = Categories.objects.get(id=cat_id)
    context = {"allCategories": get_category}
    return render(request, "adminPanel/cat_details.html", context)

@login_required
def newCategory(request):
    category_form = CategoryForm()
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect('/blogersite/allCategories/')
    context = {"form": category_form}
    return render(request, 'adminPanel/new_cat.html', context)

@login_required
def category_delete(request, cat_id):
    obj = Categories.objects.get(id=cat_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allCategories/')

@login_required
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
#           Forbidden Words           #
#######################################
@login_required
def allForbidden(request):
    all_forbidden = ForbiddenWords.objects.all()
    context = {"allForbidden": all_forbidden}
    return render(request, "adminPanel/all_forbid.html", context)
@login_required
def newForbidden(request):
    forbidden_form = ForbiddenForm()
    if request.method == "POST":
        forbidden_form = ForbiddenForm(request.POST)
        if forbidden_form.is_valid():
            forbidden_form.save()
            return HttpResponseRedirect('/blogersite/allForbidden/')
    context = {"form": forbidden_form}
    return render(request, 'adminPanel/new_forbid.html', context)

@login_required
def forbidden_delete(request, forbidden_id):
    obj = ForbiddenWords.objects.get(id=forbidden_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allForbidden/')

@login_required
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
# Tag Names
####################################################
def allTags(request):
    all_tag = TagNames.objects.all()
    context = {"allTags": all_tag}
    return render(request, "adminPanel/all_tag.html", context)

@login_required
def newTag(request):
    tag_form = TagForm()
    if request.method == "POST":
        tag_form = TagForm(request.POST)
        if tag_form.is_valid():
            tag_form.save()
            return HttpResponseRedirect('/blogersite/allTags/')
    context = {"form": tag_form}
    return render(request, 'adminPanel/new_tag.html', context)

@login_required
def tag_delete(request, tag_id):
    obj = TagNames.objects.get(id=tag_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allTags/')

@login_required
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
# Posts
####################################################

def allPosts(request):
    all_posts = Posts.objects.all()
    context = {"allPosts": all_posts}
    return render(request, "adminPanel/all_post.html", context)


def getPosts(request, post_id):
    get_posts = Posts.objects.get(id=post_id)
    context = {"allPosts": get_posts}
    return render(request, "adminPanel/post_details.html", context)

@login_required
def newPost(request):
    post_form = PostForm()
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            return HttpResponseRedirect('/blogersite/allPosts/')
    context = {"form": post_form}
    return render(request, 'adminPanel/new_post.html', context)

@login_required
def post_delete(request, post_id):
    obj = Posts.objects.get(id=post_id)
    obj.delete()
    return HttpResponseRedirect('/blogersite/allPosts/')

@login_required
def post_edit(request, post_id):
    post = Posts.objects.get(id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES,instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/blogersite/allPosts/')
    else:
        form = PostForm(instance=post)
    return render(request, 'adminPanel/new_post.html', {'form': form})


####################################################
#                Home Operations                   #
####################################################

def search(request):

    posts = Posts.objects.filter(post_title__icontains=request.GET['query'])
    try:
        tag=TagNames.objects.get(tag_name__icontains=request.GET['query'])
        posts2=Posts.objects.filter(post_tags=tag.id)
    except:
        return render(request, "hometemp/home.html",{'allPosts':posts,'allCategories':Categories.objects.all,"locksubs":1})
    else:
        return render(request, "hometemp/home.html",{'allPosts':posts2,'allCategories':Categories.objects.all,"locksubs":1})


def getCategoryPosts(request, cat_id):
    subcat = sub(request)
    get_category = Categories.objects.get(id=cat_id)
    context = {'allCategories':Categories.objects.all,"subcat": subcat,'allPosts':Posts.objects.filter(	post_cat_id=get_category.id).order_by('-post_date'),"locksubs":1}
    return render(request, "hometemp/home.html", context)



def homepost(request,hpost_id):
    userid = request.user.id
    comment = Comment.objects.filter(comment_post_id=hpost_id)
    subcat = sub(request)
    dislikescount = Userslike.objects.filter(state=0, like_post_id_id=hpost_id).count()
    likescount = Userslike.objects.filter(state=1,like_post_id_id=hpost_id).count()
    data={
        'likes':likescount,
        'dislikes':dislikescount,
    }
    try:
        return render(request,"hometemp/home_post", {"postid" : hpost_id,  "User" : userid, "Comment": comment,"likes":data,"Post_details":Posts.objects.get(id=hpost_id),'allCategories':Categories.objects.all,"subcat": subcat,"locksubs":1} )
    except Exception:
        return HttpResponseRedirect("/blogersite/home")




@csrf_exempt
def subscribe(request):

    userID = request.POST.get('userID', None)
    catID = request.POST.get('catID', None)
    Categories.user.through.objects.create(categories_id=catID, user_id=userID)
    data = {
        'success': True
    }

    cat=Categories.objects.get(id=catID)
    cat_name=cat.cat_name
    body = ' Welcome '+request.user.username+' to BlogerSite \n you have successfuly subscribed in '+cat_name+' Category'
    send_mail("Subscribtion:", body, 'blogersiteH@gmail.com', [request.user.email], fail_silently=False)

    return JsonResponse(data)



@csrf_exempt
def unsubscribe(request):
    userID = request.POST.get('userID', None)
    catID = request.POST.get('catID', None)
    Categories.user.through.objects.get(categories_id=catID, user_id=userID).delete()
    data = {
        'success': True
    }
    return JsonResponse(data)


def sub(request):

    catsub=Categories.objects.filter(user=request.user.id)
    cat_sub=[]
    for i in catsub:
        cat_sub.append(i.id)
    return cat_sub

@login_required
def like(request,post_ID):
    try:
        checker=Userslike.objects.get(like_post_id_id=post_ID,like_user_id_id=request.user.id)
    except Exception:
        Userslike.objects.create(like_post_id_id=post_ID, like_user_id_id=request.user.id, state=1)
        likes=Userslike.objects.filter(state=1,like_post_id_id=post_ID).count()
        data = {'likes': likes, }
        return render(request, "hometemp/home_post", {"likes": data, "Post_details": Posts.objects.get(id=post_ID),
                                                      'allCategories': Categories.objects.all})

    checker = Userslike.objects.get(like_post_id_id=post_ID, like_user_id_id=request.user.id)
    if checker.state == 1:
        checker.delete()

        likes = Userslike.objects.filter(state=1, like_post_id_id=post_ID).count()
        data = {'likes': likes}
        return render(request, "hometemp/home_post", {"likes":data,"Post_details": Posts.objects.get(id=post_ID),'allCategories': Categories.objects.all})
    else:
        checker.state=1
        checker.save()
        likes = Userslike.objects.filter(state=1, like_post_id_id=post_ID).count()
        data = {'likes': likes}
        return render(request, "hometemp/home_post", {"likes":data,"Post_details": Posts.objects.get(id=post_ID),'allCategories': Categories.objects.all})

@login_required
def dislike(request,post_ID):
    dislikers = Userslike.objects.filter(state=0, like_post_id_id=post_ID).count()
    if dislikers >= 9:
        Posts.objects.get(id=post_ID).delete()
        return HttpResponseRedirect("/blogersite/home")
    try:
        dischecker=Userslike.objects.get(like_post_id_id=post_ID,like_user_id_id=request.user.id)
    except Exception:
        Userslike.objects.create(like_post_id_id=post_ID, like_user_id_id=request.user.id, state=0)
        dislikes=Userslike.objects.filter(state=0,like_post_id_id=post_ID).count()
        data = {'dislikes': dislikes }
        return render(request, "hometemp/home_post", {"likes": data, "Post_details": Posts.objects.get(id=post_ID),
                                                      'allCategories': Categories.objects.all})


    dischecker = Userslike.objects.get(like_post_id_id=post_ID, like_user_id_id=request.user.id)
    if dischecker.state == 0:
        dischecker.delete()
        dislikes = Userslike.objects.filter(state=0, like_post_id_id=post_ID).count()
        data={'dislikes':dislikes}
        return render(request, "hometemp/home_post", {"likes": data, "Post_details": Posts.objects.get(id=post_ID),'allCategories': Categories.objects.all})
    else:
        dischecker.state=0
        dischecker.save()
        dislikes = Userslike.objects.filter(state=0, like_post_id_id=post_ID).count()
        data={'dislikes':dislikes}
        return render(request, "hometemp/home_post", {"likes": data, "Post_details": Posts.objects.get(id=post_ID),'allCategories': Categories.objects.all})



##################################################################
#comments & reply
#################################################################


# def getThePost(request, post_id):
#     get_posts = Posts.objects.get(id=post_id)
#     context = {"allPosts": get_posts}
#     return render(request, "adminPanel/post.html", context)
#
#
# def addComment(request, post_id):
#     print post_id, request.user
#     if request.method == 'POST':
#         comment = CommentForm(request.POST, request.FILES)
#         if comment.is_valid():
#             comment = comment.save(commit=False)
#             # return an object that hasn't yet been saved to the database to do proccessing on it
#         # comment.comment_body = wordsCleaner(comment.comment_body)
#         comment.post = Posts.objects.get(id=post_id)
#         # comment.User = User.objects.get(id = request.user.id)
#         comment.comment_user_id_id = request.user.id
#         comment.comment_post_id_id = post_id
#
#         comment.save()
#         return redirect(request.path)
#     return HttpResponseRedirect("/main/" + post_id + "/post")
#
#
# def addReply(request, post_id, commentID):
#     if request.method == 'POST':
#         reply = CommentForm(request.POST, request.FILES)
#         if reply.is_valid():
#             reply = reply.save(commit=False)
#         # reply.comment_body = wordsCleaner(reply.comment_body)
#         reply.post = Posts.objects.get(id=post_id)
#         # comment.User = User.objects.get(id = request.user.id)
#         reply.comment_user_id_id = request.user.id
#         reply.comment_post_id_id = post_id
#         reply.reply_comment_id = Comment.objects.get(id=commentID)
#
#         reply.save()
#         return redirect(request.path)
#     return HttpResponseRedirect("/main/" + post_id + "/post")

# def postPage(request, post_id):
#     get_posts = Posts.objects.get(id=post_id)
#     comment = Comment.objects.filter(comment_post_id = post_id)
#     reply = Reply.objects.filter(reply_post_id = post_id)
#     context = {"allPosts": get_posts, "Comment": comment, "Reply" : reply}
#     return render(request, "adminPanel/post.html", context)

# def postPage(request,post_id):
# 	post=Posts.objects.get(id =post_id)
# 	comment=Comment.objects.filter(id= post_id)
# 	reply=Reply.objects.filter(id= post_id)
# 	context={'postshow':post , 'comment' : comment, 'reply' : reply}
# 	return render(request, 'adminPanel/post.html' ,context)


# def addComment(request, post_id):
#     comment_post_id = Posts.objects.get(id = post_id)
#     user_id = request.user.id
#     if request.method == "POST":
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             comment = comment.save(commit=False)
#             # return an object that hasn't yet been saved to the database to do processing on it
#             comment.id = comment_post_id
#             comment.id = user_id
#             comment.checkForbidden()
#             comment.save()
#             return redirect('/blogersite/'+post_id+'/post')
#     else:
#         form = CommentForm()
#         context = {"form": form}
#     return render(request, 'adminPanel/add_comments.html', context)

# @login_required
# def addComment(request, post_id):
#     form = CommentForm()
#
#     comment_post = Posts.objects.get(id = post_id)
#     # return HttpResponse(comment_post_id)
#     # user_id = request.user.id
#     if request.method == "POST":
#         comment = CommentForm(request.POST)
#         if comment.is_valid():
#             comment = comment.save(commit=False)
#             comment.comment_post_id = comment_post
#             # comment.id = user_id
#             comment.checkForbidden()
#             comment.save()
#             return redirect('/blogersite/homepost/'+post_id)
#     else:
#         form = CommentForm()
#     context = {"form": form}
#     return render(request, 'adminPanel/add_comments.html', context)

@login_required
def addReply(request, post_id, comment_id):
    reply_comment = Posts.objects.get(id = post_id)
    comment_post = Comment.objects.get(id = comment_id)
    user_id = request.user.id
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.reply_post_id = reply_comment
            reply.reply_comment_id = comment_post
            # reply.comment_user_id = user_id
            reply.checkForbidden()
            reply.save()
            return redirect('/blogersite/'+post_id+'/post')
    else:
        form = ReplyForm()
    context = {"form": form}
    return render(request, 'adminPanel/reply_comment.html', context)

@csrf_exempt
def commentAjax(request):
    comment =request.POST['comment']

    userid =request.POST['userid']
    user = User.objects.get(id=userid)

    postid =request.POST['postid']
    post = Posts.objects.get(id=postid)

    newcomm =Comment.objects.create(comment_body=comment, comment_post_id=post , comment_user_id=user )
    newcomm.checkForbidden()
    newcomm.save()

    cont=Comment.objects.latest("comment_date")
    date = cont.comment_date
    # date =newcomm.comment_date

    return JsonResponse({'date': date})
    # return HttpResponseRedirect('/blogersite/homepost/' + postid)
    # return redirect(request,"/blogersite/homepost.html/"+postid,{"date":date})