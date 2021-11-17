from django.urls import path
from like.views import LikeView

urlpatterns = [

    path('posts/likes/', LikeView.as_view()),


]