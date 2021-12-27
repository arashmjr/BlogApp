from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from like.models import Like
from like.serializer import LikeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes


class LikeDetailView(APIView):

    def post(self, request, post):
        user_id = request.user.id

        document = Like.objects.filter(post=post, user=user_id).first()

        if document:
            if document.is_deleted:
                document.is_deleted = False
                document.save()
                return Response({
                    "data": None,
                    "message": "this post liked by user successfully",
                    "success": True
                }, status=status.HTTP_201_CREATED)
            return Response({
                "data": None,
                "message": "this user liked this post before",
                "success": False
            }, status=status.HTTP_200_OK)

        input_data = {'post': post, 'user': user_id}
        serializer = LikeSerializer(data=input_data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "data": None,
                "message": "this post liked by user successfully",
                "success": True
            }, status=status.HTTP_201_CREATED)
        return Response({
            "data": serializer.errors,
            "message": "error in process",
            "success": False
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post):

        record = Like.objects.filter(post=post, user=request.user.id).first()
        if record:
            record.is_deleted = True
            record.save()
            return Response({
                "data": None,
                "message": "your like is deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "error in process",
            "success": False
        }, status=status.HTTP_204_NO_CONTENT)

