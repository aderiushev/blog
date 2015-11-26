from django.contrib import admin
from django import forms
from redactor.widgets import RedactorEditor

from .models import Post


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
           'text': RedactorEditor(redactor_options={'plugins': ['table']}, upload_to='myblog/media/uploads/'),
        }


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm

admin.site.register(Post, PostAdmin)