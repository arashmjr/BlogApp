import datetime
from example.models import User


class PostModelDTO:
    id: str
    post_title: str
    author: str
    body: str
    created_at: datetime
    updated_at: datetime
    is_ban: bool
    is_liked: bool
    count_likes: int

    def __init__(self, id: str, post_title: str, author: str, body: str, created_at: datetime,
                 updated_at: datetime, is_ban: bool, is_liked: bool, count_likes: int):

        self.id = id
        self.post_title = post_title
        self.author = author
        self.body = body
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_ban = is_ban
        self.is_liked = is_liked
        self.count_likes = count_likes

    def to_dict(self):
        return {
                "id": self.id,
                "post_title": self.post_title,
                "author": self.author,
                "body": self.body,
                "created_at": self.created_at,
                "updated_at": self.updated_at,
                "is_ban": self.is_ban,
                "is_liked": self.is_liked,
                "count_likes": self.count_likes,
                }


