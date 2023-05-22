from django.contrib import admin
from .models import Blog, BlogComment

class BloAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_public', 'post_date', )
    list_display_links = ('id', 'name')
    search_fields = ('name', 'author')
    list_per_page = 1
    list_editable = ('is_public',)

admin.site.register(Blog, BloAdmin)
admin.site.register(BlogComment)
