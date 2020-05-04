from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("posts", views.posts, name="posts_index"),
    path("post/new", views.post_new, name="post_new"),
    path("post/edit/<int:pk>", views.post_edit, name="post_edit"),
    path("categories", views.categories, name="categories_index"),
    path("users", views.users, name="users_index"),
    path("users/edit/<int:pk>/", views.user_edit, name="user_edit"),
    path("teams", views.teams, name="teams_index"),
    path("teams/edit/<int:pk>/", views.team_edit, name="team_edit"),
]
