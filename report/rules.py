from report.config import maximumReportLimit
from report.models import Report
from post.models import Post


def is_report_duplicated(user, uuid):

    return Report.objects.filter(
        reporter_user=user,
        entity_id=uuid,
    ).exists()


def is_passed_maximum_report_limit(uuid):
    return Report.objects.filter(entity_id=uuid).count() >= maximumReportLimit



