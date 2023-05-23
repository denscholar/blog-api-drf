from django.contrib import admin
from .models import Blog, Category

class BloAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog_title', 'is_public', 'post_date', )
    list_display_links = ('id', 'blog_title')
    search_fields = ('blog_title',)
    list_per_page = 5
    list_editable = ('is_public',)

admin.site.register(Blog, BloAdmin)
admin.site.register(Category)
