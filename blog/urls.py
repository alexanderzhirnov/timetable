from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_home, name='blog_home'),  
    path('<str:slug>/', views.blog_post, name='blog_post'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)