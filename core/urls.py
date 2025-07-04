from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('login/', views.login_view),
    path('create-post/', views.create_post),
    path('posts/', views.get_all_posts),
    path('post/<int:post_id>/', views.get_single_post),
    path('post/<int:post_id>/comment/', views.comment_on_post),
]
