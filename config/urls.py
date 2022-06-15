from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    # articles Url
    path('articles/', include('articles.urls')),
    path('api/articles/', include('articles.api_urls')),
    # products Url
    path('products/', include('products.urls')),
    path('api/products/', include('products.api_urls')),

    # services Url
    path('services/', include('services.urls')),
    path('api/services/', include('services.api_urls')),

    # carts Url
    path('carts/', include('carts.urls')),
    path('api/carts/', include('carts.api_urls')),


    # userPanel Url
    path('user-panel/', include('userPanel.urls')),
    path('api/user-panel/', include('userPanel.api_urls')),

    # seller Url
    path('seller-panel/', include('sellerPanel.urls')),
    path('api/seller-panel/', include('sellerPanel.api_urls')),


    # servicePanel Url
    path('service-panel/', include('servicePanel.urls')),
    path('api/service-panel/', include('servicePanel.api_urls')),
    # Site Settings Url
    path('api/site-settings/', include('siteSettings.api_urls')),

    # contactUs Url
    path('contact-us/', include('contactUs.urls')),
    path('api/contact-us/', include('contactUs.api_urls')),
    # aboutUs Url
    path('about-us/', include('aboutUs.urls')),
    path('api/about-us/', include('aboutUs.api_urls')),


    path('accounts/', include('accounts.urls')),

    # Admin
    path('admin/', admin.site.urls,name='admin_panel'),
]


if settings.DEBUG:
    urlpatterns += urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


    urlpatterns += urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
