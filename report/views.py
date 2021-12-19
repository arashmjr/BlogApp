from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from comment.models import Comment
from report.serializer import ReportSerializer
from report.rules import is_passed_maximum_report_limit, is_report_duplicated


class ReportPostView(APIView):
    def post(self, request, uuid):
        request.data['entity_id'] = uuid
        request.data['reporter_user'] = request.user.id

        serializer = ReportSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"data": serializer.errors,
                             "message": '',
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        if Post.objects.filter(pk=uuid).last().author == request.user:
            return Response({"data": None,
                             "message": "error in process",
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        if is_report_duplicated(request.user, uuid):
            return Response({"data": None,
                             "message": "this entity reported by user before",
                             "success": False,
                             }, status=status.HTTP_409_CONFLICT)

        if is_passed_maximum_report_limit(uuid):
            desire_post = Post.objects.filter(pk=uuid).first()
            desire_post.is_ban = True
            desire_post.save()
            return Response({"data": None,
                             "message": 'success',
                             "success": True,
                             }, status=status.HTTP_200_OK)

        serializer.save()
        return Response({"data": serializer.data,
                         "message": 'success',
                         "success": True
                         }, status=status.HTTP_201_CREATED)


class ReportCommentView(APIView):
    def post(self, request, uuid):
        request.data['entity_id'] = uuid
        request.data['reporter_user'] = request.user.id

        serializer = ReportSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"data": serializer.errors,
                             "message": '',
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        if Comment.objects.filter(pk=uuid).last().user == request.user:
            return Response({"data": None,
                             "message": "error in process",
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        if is_report_duplicated(request.user, uuid):
            return Response({"data": None,
                             "message": "this post reported by user before",
                             "success": False,
                             }, status=status.HTTP_409_CONFLICT)

        if is_passed_maximum_report_limit(uuid):
            desire_comment = Comment.objects.filter(pk=uuid).first()
            desire_comment.is_ban = True
            desire_comment.save()
            return Response({"data": None,
                             "message": 'success',
                             "success": True,
                             }, status=status.HTTP_200_OK)

        serializer.save()
        return Response({"data": serializer.data,
                         "message": 'success',
                         "success": True
                         }, status=status.HTTP_201_CREATED)



