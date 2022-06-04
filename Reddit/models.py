from django.db import models
from django.utils.text import slugify
from . import validators
import uuid


class Subreddit(models.Model):
    """Name for subreddit"""
    name = models.CharField(max_length=100, unique=True, validators=[validators.CustomValidators.letters_only])

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


class Post(models.Model):
    """Temporary Model to write post on chosen subreddit"""
    # In future remodel this to work on main page and subreddit page
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)  # Remember to create text to unique url converter!!
    post = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    date_added = models.DateTimeField(auto_now=True)  # This will work locally only!!
    random_url = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        """Slugify title to use as url"""
        self.slug = slugify(self.title, allow_unicode=True)
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        """Return two representations of string models"""
        return f"{self.title, self.post, self.slug, self.random_url}"


class Comment(models.Model):
    """Model for commenting posts"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.TextField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    temporary_key = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, blank=True)

    def __str__(self):
        """Return string of comment."""
        return f"{self.comment}"
