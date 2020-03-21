# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth import login,logout,authenticate

from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def now_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('wxy:home'))

def register(request):
    if request.method != 'POST':
        form=UserCreationForm()
    else:
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            new=form.save()
            ok=authenticate(username=new.username,password=request.POST['password1'])
            
            login(request,ok)
            return HttpResponseRedirect(reverse('wxy:home'))
    context={'form':form}
    return render(request,'users/register.html',context)
            
    
