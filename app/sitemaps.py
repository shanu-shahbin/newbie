from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticSitemap(Sitemap):
    def items(self):
        return ['index', 'about', 'company_list']
    def location(self, item):
        return reverse(item)
    
class JobSitemap(Sitemap):
    def items(self):
        return ['company_list']
    def location(self, item):
        return reverse(item)
    

