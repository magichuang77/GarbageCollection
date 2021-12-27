"""GarbageCollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path, include
from django.views.static import serve
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from GarbageCollection.settings import MEDIA_ROOT
from users.views import VerifyCodeViewSet, UserViewSet

router = DefaultRouter(trailing_slash=False)  # 新建路由 trailing_slash=True代表url末尾加上’/’

# 配置发送验证码url
router.register('code', VerifyCodeViewSet, basename='code')
# 配置用户的url
router.register('users', UserViewSet, basename="users")

urlpatterns = [
    re_path("^", include(router.urls)),
    # 文件
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
    # drf文档，title自定义
    # path('docs/', include_docs_urls(title='垃圾回收平台')),
    # jwt的认证接口
    path('login/', obtain_jwt_token),
]
