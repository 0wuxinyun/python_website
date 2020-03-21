from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url(r'^subjects/$',views.subjects,name='subjects'),
    url(r'^subject/(?P<subject_id>\d+)$',views.subject,name='subject'),
    url(r'^new_subject/$',views.new_subject,name='new_subject'),
    url(r'^(?P<subject_id>\d+)/new_note$',views.new_note,name='new_note'),
    url(r'^(?P<note_id>\d+)/edit_note$',views.edit_note,name='edit_note'),
    
    ]
