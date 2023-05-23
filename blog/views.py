from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status
from blog.models import Blog, Category
from blog.serializers import BlogSerializers, CategorySerializer


class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CategoryDetailView(APIView):
    def get(self, request, pk):
        category_detail = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializer(category_detail)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class BlogListView(APIView):
    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializers(blogs, many=True)
        response = {"message": "all blogs", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BlogSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "blog created", "data": serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlogDetailView(APIView):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializers(blog)
        response = {"message": "blog details", "data": serializer.data}
        return Response(data=response, status=status.HTTP_200_OK)

    def put(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializers(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {"message": "blog updated", "data": serializer.data}
            return Response(data=response, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        blog.delete()
        response = {"message": "blog deleted", "data": {}}
        return Response(data=response, status=status.HTTP_200_OK)
