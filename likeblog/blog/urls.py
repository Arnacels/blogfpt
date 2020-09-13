from django.urls import path
from . import views

urlpatterns = [
    path('', views.ThemeView.as_view(), name='theme'),
    path('theme/<int:pk>/', views.PostView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('create-post/', views.CreatePost.as_view(), name='post_create'),
    path('edit-post/<int:pk>/', views.UpdatePost.as_view(), name='post_edit'),
    path('delete-post/<int:pk>/', views.DeletePost.as_view(), name='post_delete'),
    path('like-post/<int:pk>/', views.like_post, name='post_like')
]