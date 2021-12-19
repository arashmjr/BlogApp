from django.urls import path
from like.views import LikeDetailView, LikeListView

urlpatterns = [

    path('<post>/like/', LikeDetailView.as_view()),
    path('<post>/likes/', LikeListView.as_view()),

]

