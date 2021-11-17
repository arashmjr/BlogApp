from django.urls import path
from comment.views import CommentView, CommentDetailView, CommentDetail

urlpatterns = [
    path('<int:post>/comments/', CommentView.as_view()),
    path('<int:post>/comment/<int:comment>/', CommentDetailView.as_view()),
    path('comment/<int:comment>/', CommentDetail.as_view()),

]
