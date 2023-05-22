from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.utils import IntegrityError
from django.utils.text import slugify
import uuid


class Blog(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_public = models.BooleanField(default=False)
    post_date = models.DateField(default=date.today)
    slug = models.SlugField(max_length=1000, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name + " ==> " + str(self.author)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)[:50] if self.name else "blog"
            unique_id = uuid.uuid4().hex[
                :10
            ]  # Generate a unique identifier using UUID4
            slug = f"{base_slug}-{unique_id}"
            counter = 1
            while True:
                try:
                    self.slug = slug
                    super().save(*args, **kwargs)
                    break
                except IntegrityError:
                    # Slug already exists, modify the slug
                    slug = f"{base_slug}-{unique_id}-{counter}"
                    counter += 1
                    if (
                        counter > 1000
                    ):  # Avoid infinite loop in case of extremely high counter
                        raise ValueError("Cannot generate a unique slug.")
        else:
            super().save(*args, **kwargs)


class BlogComment(models.Model):
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)
