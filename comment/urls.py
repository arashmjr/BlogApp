from django.urls import path
from comment.views import CommentView, CommentDetailView

urlpatterns = [
    path('<int:post>/comment/', CommentView.as_view()),
    path('<int:post>/comments/<int:comment>/', CommentDetailView.as_view()),

]

