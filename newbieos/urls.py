from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from app.sitemaps import StaticSitemap, JobSitemap

sitemaps = {
    'static': StaticSitemap,
    'job': JobSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('app.urls')),
    path('',include('allauth.urls')),


]


if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)