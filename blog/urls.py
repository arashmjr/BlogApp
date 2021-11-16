from django.urls import path
from blog.views import PostView, PostDetailView

urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/<int:post>/', PostDetailView.as_view())

]
