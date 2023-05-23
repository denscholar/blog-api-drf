from rest_framework import serializers
from .models import Blog


class BlogSerializers(serializers.ModelSerializer):
    # validator
    name = serializers.StringField(required=True)
    description = serializers.StringField(required=True)

    class Meta:
        model = Blog
        fields = ("name", "description", "is_public", "post_date", "slug")
        read_only_fields = ("post_date", "slug")

    # fields level validation
    def validate_name(self, value):
        if len(value) < 4:
            raise serializers.ValidationError("blog title iss very short")

    # object level vaalidation
    def validate(self, data):
        if data["name"] == data["description"]:
            raise serializers.ValidationError("name and description can't be same")
        else:
            return data
