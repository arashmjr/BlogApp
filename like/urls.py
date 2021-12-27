from django.urls import path
from like.views import LikeDetailView

urlpatterns = [

    path('<post>/like/', LikeDetailView.as_view()),

]

