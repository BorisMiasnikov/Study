from django.db import models
from accounts.models import Author
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.TextField(unique=True)


class Post(models.Model):

    news = "N"
    article = "A"

    POSITIONS = [(news, "Новость"), (article, "Статья")]

    author = models.ForeignKey(Author, on_delete= models.CASCADE)
    choice_field = models.CharField(max_length= 1, choices=POSITIONS, default="article")
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



