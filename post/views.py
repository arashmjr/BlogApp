from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from post.models import Post
from example.models import User
from like.models import Like
from post.serializer import PostSerializer
from post.ModelDTO import PostModelDTO
from post.rules import is_post_liked_by_user, last_post_of_each_user


class PostView(APIView):  # [GET, POST, DELETE]

    def get(self, request):
        user = request.user.id

        if not Post.objects.filter(author=user, is_ban=False).exists():
            return Response({"data": '',
                             "message": "There is no post for this user",
                             "success": False,
                             }, status=status.HTTP_204_NO_CONTENT)
        print(Post.objects.filter(author=user, is_ban=False))
        data = []
        for item in Post.objects.filter(author=user, is_ban=False):
            count_likes = Like.objects.filter(post=item.id, is_deleted=False).count()
            if is_post_liked_by_user(item.id, request.user):
                model = PostModelDTO(item.id, item.post_title, item.author, item.body, item.created_at, item.updated_at,
                                     item.is_ban, True, count_likes)
                data.append(model.to_dict())
            if not is_post_liked_by_user(item.id, request.user):
                model = PostModelDTO(item.id, item.post_title, item.author, item.body, item.created_at, item.updated_at,
                                     item.is_ban, False, count_likes)
                data.append(model.to_dict())
        return Response({
            "data": str(data),
            "message": "success"},
            status=status.HTTP_200_OK)

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
        desire_post = Post.objects.filter(pk=post, is_ban=False).last()
        count_likes = Like.objects.filter(post=post, is_deleted=False).count()
        if is_post_liked_by_user(post, request.user):
            model = PostModelDTO(desire_post.id, desire_post.post_title, desire_post.author, desire_post.body,
                                 desire_post.created_at, desire_post.updated_at, desire_post.is_ban, True, count_likes)
            return Response({
                "data": str(model.to_dict()),
                "success": True
            }, status=status.HTTP_200_OK)

        model = PostModelDTO(desire_post.id, desire_post.post_title, desire_post.author, desire_post.body,
                             desire_post.created_at, desire_post.updated_at, desire_post.is_ban, False, count_likes)
        return Response({
            "data": str(model.to_dict()),
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


class HomePagePostView(APIView):
    # display last of post each author in home
    def get(self, request):
        users = User.objects.all()
        recent_posts = last_post_of_each_user(users)

        data = []
        for item in recent_posts:
            count_likes = Like.objects.filter(post=item.id, is_deleted=False).count()

            if is_post_liked_by_user(item.id, request.user):
                model = PostModelDTO(item.id, item.post_title, item.author, item.body, item.created_at,
                                     item.updated_at, item.is_ban, True, count_likes)
                data.append(model.to_dict())

            if not is_post_liked_by_user(item.id, request.user):
                model = PostModelDTO(item.id, item.post_title, item.author, item.body, item.created_at, item.updated_at,
                                     item.is_ban, False, count_likes)
                data.append(model.to_dict())

        return Response({
            "data": str(data),
            "message": "success"},
            status=status.HTTP_200_OK)

