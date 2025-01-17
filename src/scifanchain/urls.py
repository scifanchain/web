from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static

from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


# for DRF Routers
# Routers provide an easy way of automatically determining the URL conf.
from works.views import StageViewSet
from authors.views import UserViewSet, WalletViewSet
from blogs.views import PostViewSet, CategoryViewSet
from community.views import ChannelViewSet, TopicViewSet, ReplylViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('stages', StageViewSet)
router.register('wallets', WalletViewSet)
router.register('channels', ChannelViewSet)
router.register('topics', TopicViewSet)
router.register('replies', ReplylViewSet)
router.register('blogs/posts', PostViewSet)
router.register('blogs/categories', CategoryViewSet)

# for Django Web Routers
urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('coming/', views.coming, name='coming'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),
    path('blogs/', include('blogs.urls'), name='blogs'),
    path('works/', include('works.urls'), name='works'),
    path('authors/', include('authors.urls'), name='authors'),
    path('community/', include('community.urls'), name='community'),
    path('mdeditor/', include('mdeditor.urls')),
    path('summernote/', include('django_summernote.urls')),

    # api
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/register/', views.register, name='register'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 后台管理覆写
admin.site.site_title = settings.SITE_NAME
admin.site.site_header = settings.SITE_NAME
