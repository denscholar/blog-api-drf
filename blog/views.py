from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from blog.models import Blog
from blog.serializers import BlogSerialisers


@api_view(["GET", "POST"])
def blog_list(request, format=None):
    if request.method == "GET":
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerialisers(blogs, many=True)
        response = {
            "message": "all blogs",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = BlogSerialisers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def blog_detail(request, pk):
    blog = Blog.objects.get(pk=pk)
    serializer = BlogSerialisers(blog)
    response = {
        "message": "single blog",
        "data": serializer.data,
    }
    return Response(data=response, status=status.HTTP_200_OK)
