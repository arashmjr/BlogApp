from django.urls import path
from post.views import PostView, PostDetailView, HomePagePostView
from django.conf.urls import include

urlpatterns = [
    path('posts/', PostView.as_view()),
    path('posts/homepage/', HomePagePostView.as_view()),
    path('posts/<post>/', PostDetailView.as_view()),
    path('posts/', include('comment.urls')),
    path('posts/', include('like.urls')),
    path('posts/', include('report.urls')),

]
