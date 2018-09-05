from django.contrib import sitemaps
from django.core.urlresolvers import reverse

#sitemap
#see https://docs.djangoproject.com/en/1.11/ref/contrib/sitemaps/#creating-a-sitemap-index
class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home',]

    def location(self, item):
        return reverse(item)
