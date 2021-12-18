from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from report.models import ReportPost, ReportComment
from post.models import Post
from comment.models import Comment
from report.serializer import ReportPostSerializer, ReportCommentSerializer
from report.rules import is_passed_maximum_report_post_limit, is_report_duplicated


class ReportPostView(APIView):
    def post(self, request, post):
        request.data['post'] = post
        request.data['reporter_user'] = request.user.id

        serializer = ReportPostSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({"data": serializer.errors,
                             "message": '',
                             "success": False,
                             }, status=status.HTTP_400_BAD_REQUEST)

        if is_report_duplicated(request.user, post):
            return Response({"data": None,
                             "message": "this post reported by user before",
                             "success": False,
                             }, status=status.HTTP_409_CONFLICT)

        if is_passed_maximum_report_post_limit(post):
            desire_post = Post.objects.filter(pk=post).first()
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
    pass


# class ReportView(APIView):
#     def post(self, request, entity_type, entity, reason_type):
#
#         request.data['entity_id'] = entity
#         request.data['entity_type'] = entity_type
#         request.data['reason_type'] = reason_type
#         request.data['reporter_user'] = request.user.id
#
#         if Report.objects.filter(
#                 reporter_user=request.user,
#                 entity_id=entity, entity_type=entity_type
#         ).exists():
#             return Response({"data": None,
#                              "message": "this entity reported by user before",
#                              "success": False,
#                              }, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = ReportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#
#             count_obj = Report.objects.filter(
#                 entity_id=entity, entity_type=entity_type
#             ).count()
#             print('count is here', count_obj)
#             if count_obj >= 100:
#                 if entity_type == EntityType.post:
#                     ban_post = Post.objects.filter(post=entity).first()
#                     ban_post.is_ban = True
#                     ban_post.save()
#                     return Response({"data": serializer.data,
#                                      "message": '',
#                                      "success": True
#                                      }, status=status.HTTP_200_OK)
#
#                 ban_cm = Comment.objects.filter(comment=entity)
#                 ban_cm.is_ban = True
#                 ban_cm.save()
#                 return Response({"data": serializer.data,
#                                  "message": '',
#                                  "success": True
#                                  }, status=status.HTTP_200_OK)
#
#             return Response({"data": serializer.data,
#                              "message": '',
#                              "success": True
#                              }, status=status.HTTP_200_OK)
#
#         return Response({"data": serializer.errors,
#                          "message": '',
#                          "success": False,
#                          }, status=status.HTTP_400_BAD_REQUEST)
