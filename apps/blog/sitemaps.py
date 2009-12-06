# -*- mode: python; coding: utf-8; -*-

from datetime import datetime as dt

from django.contrib.sitemaps import Sitemap

from blog.models import Post
from lib.helpers import reverse
from tagging.models import Tag, TaggedItem


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Post.objects.exclude(date__gt=dt.now())

    def lastmod(self, obj):
        return obj.date


class IndexSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        return ["post_list"]

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        if obj == "post_list":
            return Post.objects.exclude(date__gt=dt.now()).latest('date').date


class BlogTagsSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Tag.objects.usage_for_queryset(Post.objects.exclude(date__gt=dt.now()))

    def location(self, obj):
        return reverse('post_by_tag', tag=obj.name)

    def lastmod(self, obj):
        return TaggedItem.objects.get_by_model(Post.objects.exclude(
                date__gt=dt.now()), [obj.name]).latest('date').date
