# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Subject, Note

from django.http import HttpResponseRedirect,Http404

from django.core.urlresolvers import reverse

from .forms import SubjectForm,NoteForm

from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,'wxy/home.html')

@login_required
def subjects(request):
  
    subjects=Subject.objects.filter(owner=request.user).order_by('date')
    
    context={'subjects':subjects}


    return render(request,'wxy/subjects.html',context)
         
    
def subject(request,subject_id):
    subject=Subject.objects.get(id=subject_id)
    if request.user!=subject.owner:
        raise Http404        

    notes=subject.note_set.order_by('-date')
    context={'subject':subject,'notes':notes}
    
    return render(request,'wxy/subject.html',context)

def new_subject(request):
    if request.method != 'POST':
        form=SubjectForm()
    else:
        form=SubjectForm(data=request.POST)
        if form.is_valid():
            newone=form.save(commit=False)
            newone.owner=request.user
            newone.save()
            return HttpResponseRedirect(reverse('wxy:subjects'))
    context={'form':form}
    return render(request,'wxy/new_subject.html',context)

def new_note(request,subject_id):
    subject=Subject.objects.get(id=subject_id)
    if request.method != 'POST':
        form=NoteForm()
    else:
        form=NoteForm(data=request.POST)
        if form.is_valid():
            new_form=form.save(commit=False)
            new_form.subject=subject
            new_form.save()
            return HttpResponseRedirect(reverse('wxy:subject',args=[subject_id]))
    context={'form':form,'subject':subject}
    return render(request,'wxy/new_note.html',context)

def edit_note(request,note_id):
    note=Note.objects.get(id=note_id)
    subject=note.subject
    if request.user!=subject.owner:
        raise Http404        

    
    if request.method != 'POST':
        form=NoteForm(instance=note)
    else:
        form=NoteForm(instance=note,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('wxy:subject',args=[subject.id]))
    context={'note':note,'subject':subject,'form':form}
    return render(request,'wxy/edit_note.html',context)
            
        
