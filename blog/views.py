from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status


from blog.models import Blog
from blog.serializers import BlogSerializers


@api_view(["GET", "POST"])
def blog_list(request, format=None):
    if request.method == "GET":
        blogs = Blog.objects.filter(is_public=True)
        serializer = BlogSerializers(blogs, many=True)
        response = {
            "message": "all blogs",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)

    if request.method == "POST":
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def blog_detail(request, pk):
    if request.method == "GET":
        blog = Blog.objects.get(pk=pk)
        serializer = BlogSerializers(blog)
        response = {
            "message": "single blog",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)
    
    if request.method == "PUT":
        instance = get_object_or_404(Blog, pk=pk)
        serializer = BlogSerializers(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        instance = get_object_or_404(Blog, pk=pk)
        instance.delete()
        response = {
            "message": "blog deleted",
        }
        return Response(data=response, status=status.HTTP_204_NO_CONTENT)
        
