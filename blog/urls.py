
from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.BlogListView.as_view(), name='blog-list'),
    path('blog_detail/<slug:slug>/', views.BlogDetailView.as_view() , name='blog_detail'),
]
