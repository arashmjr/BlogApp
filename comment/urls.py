from django.urls import path
from comment.views import CommentView, CommentDetailView

urlpatterns = [
    path('<post>/comment/', CommentView.as_view()),
    path('<post>/comments/<comment>/', CommentDetailView.as_view()),

]

