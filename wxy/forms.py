

from django import forms

from .models import Subject,Note

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=['text']
        labels={'text':''}


class NoteForm(forms.ModelForm):
    class Meta:
        model=Note
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':100})}
    
    
