from django.urls import path
from report.views import ReportPostView, ReportCommentView

urlpatterns = [
    path('<uuid>/report/', ReportPostView.as_view()),
    path('comments/<uuid>/report/', ReportCommentView.as_view())

]


