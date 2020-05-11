from django.urls import path, include
from . import views

app__name = 'posts'

url_patterns = [
    path('', views.PostList.as_view(), name='all'),
    path('new/', views.CreatePost.as_view(), name='create'),
    path('by/<username>', views.UserPost.as_view(), name='for_user'),
    path('by/<username>/<pk>', views.PostDetail.as_view(), name='single'),
    path('delete/<pk>', views.DeletePost.as_view(), name='delete'),
]