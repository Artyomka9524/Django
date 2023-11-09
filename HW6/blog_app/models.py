from datetime import datetime

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField(null=True, blank=True)

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="articles"
    )
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)

    def views_count(self):
        self.views += 1
        self.save()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="comments"
    )
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def updated(self):
        return self.updated_at != self.created_at