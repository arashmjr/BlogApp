from django.urls import path
from blog.views import PostView, PostDetailView
from django.conf.urls import url, include

urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/<int:post>/', PostDetailView.as_view()),
]
