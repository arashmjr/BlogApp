from django.urls import path
from report.views import ReportView
from django.conf.urls import url, include

urlpatterns = [
    path('<int:entity>/<int:entity_type>/<int:reason_type>/', ReportView.as_view())
]

