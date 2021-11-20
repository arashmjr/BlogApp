from django.urls import path
from report.views import ReportView
from django.conf.urls import url, include

urlpatterns = [
    path('<int:post>/report/', ReportView.as_view())
]
