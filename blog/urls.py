from django.urls import path
from blog.views import PostView, PostDetailView
from django.conf.urls import include

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/<int:post>/', PostDetailView.as_view()),

]
