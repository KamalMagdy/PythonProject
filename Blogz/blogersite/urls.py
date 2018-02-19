from django.conf.urls import url
from django.contrib import admin
from blogersite import views
from . import views

# from django.contrib.auth import User

urlpatterns = [
    url(r'^Dashboard/$', views.managerPanel),

    url(r'^allCategories/$', views.allCategories),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/show$', views.getCategory),
    url(r'^adminPanel/new_cat/$', views.newCategory),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/edit$', views.category_edit),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/delete$', views.category_delete),

    url(r'^allForbidden/$', views.allForbidden),
    #url(r'^(?P<cat_id>[0-9]+)$', views.getCategory),
    url(r'^adminPanel/new_forbid/$', views.newForbidden),
    url(r'^adminPanel/(?P<forbidden_id>[0-9]+)/editF$', views.forbidden_edit),
    url(r'^adminPanel/(?P<forbidden_id>[0-9]+)/deleteF$', views.forbidden_delete),

    url(r'^allTags/$', views.allTags),
    url(r'^adminPanel/new_tag/$', views.newTag),
    url(r'^adminPanel/(?P<tag_id>[0-9]+)/editT$', views.tag_edit),
    url(r'^adminPanel/(?P<tag_id>[0-9]+)/deleteT$', views.tag_delete),

    url(r'^allPosts/$', views.allPosts),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/showP$', views.getPosts),
    url(r'^adminPanel/new_post/$', views.newPost),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/editP$', views.post_edit),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/deleteP$', views.post_delete),

    url(r'^admin', views.admin),
    url(r'^login$', views.login_form),
    url(r'^logged_in_only$', views.logged_in_only),
    url(r'^home$', views.home),
    url(r'^register$', views.register),
    url(r'^allusers/$', views.all_users),
    url(r'^block/(?P<usr_id>[0-9]+$)', views.block),
    url(r'^unblock/(?P<usr_id>[0-9]+$)', views.unblock),
    url(r'^promote/(?P<usr_id>[0-9]+$)', views.promote),
    url(r'^update/(?P<usr_id>[0-9]+$)', views.update),
    url(r'^delete/(?P<usr_id>[0-9]+$)', views.delete),
    url(r'^addnew/', views.addnew),
    url(r'^search/$', views.search),
    url(r'^cat/(?P<cat_id>[0-9]+$)', views.getCategoryPosts),
    url(r'^logout$', views.logout),
    url(r'^home2$', views.home2),
    url(r'^homepost/(?P<hpost_id>[0-9]+$)$', views.homepost),
    url(r'^subscribe/$', views.subscribe),
    url(r'^unsubscribe/$', views.unsubscribe),
    url(r'^like/(?P<post_ID>[0-9]+$)', views.like),
    url(r'^dislike/(?P<post_ID>[0-9]+$)', views.dislike),
]