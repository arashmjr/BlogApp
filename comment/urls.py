from django.urls import path
from comment.views import CommentView, CommentDetailView, CommentDetail

urlpatterns = [
    path('post/<int:post>/comment/', CommentView.as_view()),
    path('post/<int:post>/comment/<int:comment>/', CommentDetailView.as_view()),
    path('post/comment/<int:comment>/', CommentDetail.as_view()),

]
