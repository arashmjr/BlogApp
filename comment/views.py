from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from comment.models import Comment
from blog.models import Post
from comment.serializer import CommentSerializer
from  django.contrib.auth.mixins import PermissionRequiredMixin


@permission_classes((AllowAny,))
class CommentView(APIView):
    permission_required = ''

    # get comments of a post
    def get(self, post):
        records = Comment.objects.filter(post__id=post)
        if records:
            serializer = CommentSerializer(records, many=True)
            return Response({
                "data": serializer.data,
                "success": True
            }, status=status.HTTP_200_OK)
        return Response({"data": None,
                         "message": "this post has no comments",
                         "success": True
                         }, status=status.HTTP_200_OK)

    # post a comment
    def post(self, request, post):
        request.data['post'] = post
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": serializer.data,
                "message": "your comment is submit",
                "success": True
            }, status=status.HTTP_201_CREATED)
        return Response({
            "data": serializer.errors,
            "message": "error in process",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((AllowAny,))
class CommentDetailView(APIView):
    # get reply's of comment
    def get(self, request, post, comment):
        print('salam')
        records = Comment.objects.filter(post__id=post, replied_id=comment)
        print(records)
        if records:
            serializer = CommentSerializer(records, many=True)
            return Response({
                "data": serializer.data,
                "success": True
            }, status=status.HTTP_200_OK)
        return Response({"data": None,
                         "message": "this cm has no reply",
                         "success": True,
                         }, status=status.HTTP_204_NO_CONTENT)

    # reply to comment
    def post(self, request, post, comment):

        record = Comment.objects.filter(id=comment, post__id=post).first()
        if record:
            record.has_replied = True
            record.save()
            request.data['replied_id'] = record.id
            request.data['post'] = post
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                return Response({
                    "data": serializer.data,
                    "message": "your comment is submit",
                    "success": True
                }, status=status.HTTP_201_CREATED)

            return Response({
                "data": serializer.errors,
                "message": "error in process",
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "data": None,
            "message": "this comment does not exist",
            "success": False
        }, status=status.HTTP_204_NO_CONTENT)

    # verify comments
    # @group_required('author')
    def put(self, request, post, comment):

        request.data['post'] = post
        request.data['id'] = comment
        if Comment.objects.filter(id=comment, post=post).exists():
            record = Comment.objects.filter(id=comment, post=post).last()
            record.is_verified = True
            record.save()
            return Response({"data": '',
                             "message": 'desired comment is verified',
                             "success": True,
                             }, status=status.HTTP_200_OK)
        return Response({
            "data": '',
            "message": "error in process",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)


class CommentDetail(APIView):

    # remove a comment
    def delete(self, comment):
        record = Comment.objects.filter(id=comment)
        if record:
            record.delete()
            return Response({
                "data": None,
                "message": "your comment is deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "your comment does not exist.",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)

