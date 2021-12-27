from like.models import Like
from post.models import Post


def is_post_liked_by_user(post, user):
    return Like.objects.filter(post=post, user=user).exists()


def last_post_of_each_user(users):
    list_posts = []
    for item in users:
        last_post = Post.objects.filter(author=item.id, is_ban=False).last()
        list_posts.append(last_post)

    return list(filter(lambda x: x is not None, list_posts))

