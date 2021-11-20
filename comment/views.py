from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from comment.models import Comment
from comment.serializer import CommentSerializer
from django.db.models import Q


class CommentView(APIView):

    # get comments of a post
    def get(self, request, post):
        records = Comment.objects.filter(post__id=post, is_verified=True)
        if records:
            serializer = CommentSerializer(records, many=True)
            return Response({
                "data": serializer.data,
                "success": True
            }, status=status.HTTP_200_OK)
        return Response({"data": None,
                         "message": "this post has no comments",
                         "success": True
                         }, status=status.HTTP_204_NO_CONTENT)

    # create a comment
    def post(self, request, post):
        request.data['user'] = request.user.id
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


class CommentDetailView(APIView):
    # Allow any who authorize can get reply's
    # get reply's of comment
    def get(self, request, post, comment):
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

    # Allow any who authorize can submit reply
    # reply to comment
    def post(self, request, post, comment):

        record = Comment.objects.filter(id=comment, post__id=post).first()
        if record:
            record.has_replied = True
            record.save()
            request.data['replied_id'] = record.id
            request.data['post'] = post
            request.data['user'] = request.user.id
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

    # author of post can is verified
    # verify comments
    def put(self, request, post, comment):
        request.data['post'] = post
        request.data['id'] = comment

        if Comment.objects.filter(id=comment, post__author=request.user).exists():
            record = Comment.objects.filter(id=comment, post__author=request.user).last()
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
            }, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, post, comment):

        record = Comment.objects.filter(
                Q(id=comment, post=post, post__author=request.user) |
                Q(id=comment, post=post, user=request.user)
              )

        if record:
            record.delete()
            return Response({
                "data": None,
                "message": "your comment is deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "error in process.",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)



