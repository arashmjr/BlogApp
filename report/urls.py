from django.urls import path
from report.views import ReportPostView, ReportCommentView
from django.conf.urls import include

urlpatterns = [
    # path('<int:entity>/<int:entity_type>/<int:reason_type>/', ReportView.as_view())
    path('<int:post>/report/', ReportPostView.as_view()),
    path('comments/<int:comment>/report/', ReportCommentView.as_view())

]

