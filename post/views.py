from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from post.serializer import PostSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes


class PostView(APIView):  # [GET, POST, DELETE]

    def get(self, request):
        user = request.user.id
        # get user posts
        records = Post.objects.filter(author=user, is_ban=False)
        if records:
            serializer = PostSerializer(records, many=True)
            return Response({
                "data": serializer.data,
                "success": True
                }, status=status.HTTP_200_OK)
        return Response({
            "data": None,
            "success": False
        }, status=status.HTTP_204_NO_CONTENT)

    # create a post
    def post(self, request):
        author = request.user.id
        request.data['author'] = author
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data,
                             "success": True
                             }, status=status.HTTP_201_CREATED)
        return Response({"data": 'serializer.errors',
                        "success": False,
                        }, status=status.HTTP_400_BAD_REQUEST)

    # remove all posts of user
    # remove user posts
    def delete(self, request):
        records = Post.objects.filter(author=request.user)
        if records:
            records.delete()
            return Response({
                "data": None,
                "message": "your posts are deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "you have no post.",
            "success": False
        }, status=status.HTTP_204_NO_CONTENT)


class PostDetailView(APIView):  # [GET, PUT, DELETE]

    def get(self, request, post):

        if not Post.objects.filter(pk=post, is_ban=False).exists():
            return Response({"data": '',
                             "message": "this post is not exist",
                             "success": False,
                             }, status=status.HTTP_204_NO_CONTENT)
        serializer = PostSerializer(Post.objects.filter(pk=post, is_ban=False).last())
        return Response({
            "data": serializer.data,
            "success": True
        }, status=status.HTTP_200_OK)

    def put(self, request, post):
        request.data['author'] = request.user.id
        if Post.objects.filter(id=post, author=request.user, is_ban=False).exists():
            record = Post.objects.filter(id=post, author=request.user, is_ban=False).last()
            serializer = PostSerializer(record, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data": serializer.data,
                                "success": True,
                                 }, status=status.HTTP_200_OK)

            return Response({"data": serializer.errors,
                             "success": False,
                            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": '',
                         "message": "this post is not exist",
                         "success": False,
                         }, status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, post):
        record = Post.objects.filter(pk=post, author=request.user).first()
        if record:
            record.delete()
            return Response({
                "data": None,
                "message": "your post is deleted.",
                "success": True
            }, status=status.HTTP_200_OK)

        return Response({
            "data": None,
            "message": "your post does not exist.",
            "success": False
        }, status=status.HTTP_204_NO_CONTENT)


# class HomePagePostView(APIView):
#     # display last of post each author in home
#     def get(self, request):
#         users = User.objects.all()
#         list_post = []
#         for item in users:
#             last_post = Post.objects.filter(author=item.id).last()
#             list_post.append(last_post)
#
#         filtered_data = filter(lambda x: x is not None, list_post)
#         serializer = PostSerializer(filtered_data, many=True)
#         return Response({
#             "data": serializer.data,
#             "message": "success"},
#             status=status.HTTP_200_OK)
