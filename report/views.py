from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from report.models import Report
from blog.models import Post
from comment.models import Comment
from report.serializer import ReportSerializer


class ReportView(APIView):
    def post(self, request, entity_type, entity, reason_type):

        request.data['entity_id'] = entity
        request.data['entity_type'] = entity_type
        request.data['reason_type'] = reason_type
        request.data['reporter_user'] = request.user.id

        if Report.objects.filter(
                reporter_user=request.user,
                entity_id=entity, entity_type=entity_type
            ).exists():
            return Response({"data": None,
                             "message": "this entity reported by user before",
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            count_obj = Report.objects.filter(
                entity_id=entity, entity_type=entity_type
            ).count()
            print('count is here', count_obj)
            if count_obj >= 100:
                if entity_type == 0:
                    ban_post = Post.objects.filter(post=entity).first()
                    ban_post.is_ban = True
                    ban_post.save()
                    return Response({"data": serializer.data,
                                     "message": '',
                                    "success": True
                                    }, status=status.HTTP_200_OK)

                if entity_type == 1:
                    ban_cm = Comment.objects.filter(comment=entity)
                    ban_cm.is_ban = True
                    ban_cm.save()
                    return Response({"data": serializer.data,
                                     "message": '',
                                     "success": True
                                     }, status=status.HTTP_200_OK)

            return Response({"data": serializer.data,
                             "message": '',
                             "success": True
                             }, status=status.HTTP_200_OK)

        return Response({"data": serializer.errors,
                         "message": '',
                         "success": False,
                         }, status=status.HTTP_400_BAD_REQUEST)
