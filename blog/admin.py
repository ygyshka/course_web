from django.contrib import admin

from blog.models import Blog
from blog.services import get_blogs_cache


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    get_blogs_cache()
    list_display = ('id', 'title', 'content', 'picture', 'date_publish')

