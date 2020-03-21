from django.conf.urls import url
from django.contrib.auth.views import login
from . import views


urlpatterns=[
    url('^login/$',login,{'template_name':'users/login.html'},name='login'),
    url('^logout/$',views.now_logout,name='now_logout'),
    url(r'^register/$',views.register,name='register'),
    

    ]

