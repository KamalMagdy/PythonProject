from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^manager/$', views.managerPanel),

    url(r'^allCategories/$', views.allCategories),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/show/$', views.getCategory),
    url(r'^adminPanel/new_cat/$', views.newCategory),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/edit/$', views.category_edit),
    url(r'^adminPanel/(?P<cat_id>[0-9]+)/delete/$', views.category_delete),

    url(r'^allForbidden/$', views.allForbidden),
    #url(r'^(?P<cat_id>[0-9]+)$', views.getCategory),
    url(r'^adminPanel/new_forbid/$', views.newForbidden),
    url(r'^adminPanel/(?P<forbidden_id>[0-9]+)/editF/$', views.forbidden_edit),
    url(r'^adminPanel/(?P<forbidden_id>[0-9]+)/deleteF/$', views.forbidden_delete),

    url(r'^allTags/$', views.allTags),
    url(r'^adminPanel/new_tag/$', views.newTag),
    url(r'^adminPanel/(?P<tag_id>[0-9]+)/editT/$', views.tag_edit),
    url(r'^adminPanel/(?P<tag_id>[0-9]+)/deleteT/$', views.tag_delete),

    url(r'^allPosts/$', views.allPosts),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/showP/$', views.getPosts),
    url(r'^adminPanel/new_post/$', views.newPost),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/editP/$', views.post_edit),
    url(r'^adminPanel/(?P<post_id>[0-9]+)/deleteP/$', views.post_delete),

]