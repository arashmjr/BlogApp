from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from like.models import Like
from like.serializer import LikeSerializer


class LikeView(APIView):

    def get(self, request):
        post_id = int(request.query_params.get('post'))
        user_id = request.user.id

        if user_id is not None and post_id is not None:

            record = Like.objects.filter(user__id=user_id, post__id=post_id, is_deleted=False).first()
            if record:
                serializer = LikeSerializer(record)
                return Response({
                    "data": serializer.data,
                    "message": f"This post was liked by user with user_id {user_id} ",
                    "success": True
                }, status=status.HTTP_200_OK)
            return Response({
                "data": None,
                "message": "This post was not liked by user",
                "success": False
            }, status=status.HTTP_200_OK)

        if post_id is not None:
            record = Like.objects.filter(post__id=post_id)
            serializer = LikeSerializer(record, many=True)
            if record:
                count = len(serializer.data)
                return Response({
                    "data": None,
                    "message": f"number of like for this post: {count}",
                    "success": True
                }, status=status.HTTP_200_OK)
            return Response({
                "data": None,
                "message": "this post does not exist",
                "success": False
            }, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, post):
        user_id = request.user.id

        document = Like.objects.filter(post__id=post, user__id=user_id).first()
        print(document)
        if document:
            if document.is_deleted == True:
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
        else:
            validate_data = {'post': post, 'user': user_id}
            serializer = LikeSerializer(data=validate_data)
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

    def delete(self, request):
        post = request.query_params.get('post')
        user = request.query_params.get('user')
        record = Like.objects.get(post__id=post, user__id=user)
        if record:
            record.is_deleted = True
            record.save()
            return Response({
                "data": None,
                "message": "your like is deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

