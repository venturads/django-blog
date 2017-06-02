from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length = 40, unique = True)
    email = models.EmailField(max_length = 100, unique = True)
    active = models.BooleanField(default = False)
    created_on = models.DateTimeField(auto_now_add=True)
    last_logged_in = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name + " : " + self.email
    
class Category(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(max_length = 100, unique = True)
    author = models.ForeignKey(Author)
    def __str__(self):
         return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    slug = models.SlugField(max_length = 100, unique = True)
    author = models.ForeignKey(Author)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length = 150, unique = True)
    slug = models.SlugField(unique = True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(Author)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title