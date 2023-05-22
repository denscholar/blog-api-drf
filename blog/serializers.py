from rest_framework import serializers
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('name', 'description', 'is_public', 'post_date', 'slug')
        read_only_fields = ('post_date', 'slug')