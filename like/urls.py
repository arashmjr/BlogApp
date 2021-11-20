from django.urls import path
from like.views import LikeDetailView, LikeListView

urlpatterns = [

    path('<int:post>/like/', LikeDetailView.as_view()),
    path('<int:post>/likes/', LikeListView.as_view()),

]
