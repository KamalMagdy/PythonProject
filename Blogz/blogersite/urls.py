from django.conf.urls import url
from django.contrib import admin
from blogersite import views

urlpatterns=[
    url(r'^admin/',admin.site.urls),
    url(r'^login$',views.login_form),
    url(r'^logged_in_only$',views.logged_in_only),
    url(r'^home$',views.home),
    url(r'^categories$',views.home),
    url(r'^post_desc$',views.home),
    url(r'^register$',views.register),
]