from report.config import maximumReportLimit
from report.models import ReportPost
from post.models import Post


def is_report_duplicated(user, post):

    return ReportPost.objects.filter(
        reporter_user=user,
        post=post,
    ).exists()


def is_passed_maximum_report_post_limit(post):
    return ReportPost.objects.filter(post=post).count() >= maximumReportLimit



