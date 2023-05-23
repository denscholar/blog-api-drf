from rest_framework import serializers
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    # validator
    blog_title = serializers.CharField(required=True)
    blog_description = serializers.CharField(required=True)

    class Meta:
        model = Blog
        fields = ("blog_title", "blog_description", "is_public", "post_date", "category" ,"slug")
        read_only_fields = ("post_date", "slug")

    # fields level validation
    def validate_blog_title(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("blog title iss very short")

    # object level vaalidation
    def validate(self, data):
        if data["blog_title"] == data["blog_description"]:
            raise serializers.ValidationError("name and description can't be same")
        else:
            return data
