from django import forms
from www.models import Post, User, Team


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("author", "title", "text", "published_date", "category", "cover")


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "tag", "status", "captain")
