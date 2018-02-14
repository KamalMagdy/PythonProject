from django.conf.urls import url
from django.contrib import admin
from blogersite import views
# from django.contrib.auth import User

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url(r'^login$',views.login_form),
    url(r'^logged_in_only$',views.logged_in_only),
    url(r'^home$',views.home),
    url(r'^categories$',views.home),
    url(r'^post_desc$',views.home),
    url(r'^register$',views.register),
    url(r'^allusers$',views.all_users),
    url(r'^block/(?P<usr_id>[0-9]+$)',views.block),
    url(r'^unblock/(?P<usr_id>[0-9]+$)',views.unblock),
    url(r'^promote/(?P<usr_id>[0-9]+$)',views.promote),
    url(r'^update/(?P<usr_id>[0-9]+$)',views.update),
    url(r'^delete/(?P<usr_id>[0-9]+$)',views.delete),
    url(r'^addnew/',views.addnew),
]