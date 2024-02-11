from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from news.models import *
from django.db.models.functions import Coalesce

class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # post_rating = Post.objects.filter(author= self).aggregate(Sum("rating"))
        # user_comments_rating = Comment.objects.filter(user = self.user).aggregate(Sum("rating"))
        # post_comments_rating = Comment.objects.filter(post__author = self).aggregate(Sum("rating"))

        post_rating = 0
        user_comments_rating = 0
        post_comments_rating = 0

        post = Post.objects.filter(author= self)
        for p in post:
            post_rating += p.rating

        user_comments = Comment.objects.filter(user = self.user)
        for u in user_comments:
            user_comments_rating += u.rating

        post_comments = Comment.objects.filter(post__author = self)
        for pc in post_comments:
            post_comments_rating += pc.rating
        print(post_rating)
        print("-------------")
        print(user_comments_rating)
        print("-------------")
        print(post_comments_rating)
        self.rating = post_rating * 3 + user_comments_rating + post_comments_rating
        self.save()




