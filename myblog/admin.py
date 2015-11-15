from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor
import blog.settings as settings

from .models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
           'text': RedactorEditor(
               upload_to='myblog/static/uploads'
           ),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)