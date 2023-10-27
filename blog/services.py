from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_blogs_cache():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = Blog.objects.all()
            cache.set(key, blog_list)
    else:
        blog_list = Blog.objects.all()

    return blog_list
