
from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.BlogListView.as_view(), name='blog-list'),
    path('blog_detail/<slug:slug>/', views.BlogDetailView.as_view() , name='blog_detail'),
    path('category-list/', views.CategoryListView.as_view() , name='category-list'),
    path('category-detail/<int:pk>/', views.CategoryDetailView.as_view() , name='category-detail'),
]
