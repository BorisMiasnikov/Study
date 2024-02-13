from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
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

        self.rating = post_rating * 3 + user_comments_rating + post_comments_rating
        self.save()


class Category(models.Model):
    category = models.TextField(unique=True)


class Post(models.Model):

    news = "N"
    article = "A"

    POSITIONS = [(news, "Новость"), (article, "Статья")]

    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    choice_field = models.CharField(max_length= 1, choices=POSITIONS, default=article)
    data_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=3000)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:125] + "..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete= models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    text = models.CharField(max_length=1000)
    data_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()



