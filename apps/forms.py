# myapp/forms.py
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminTao.models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class BlogPostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'content']