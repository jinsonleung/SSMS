import xadmin
from django.urls import path,re_path
from django.conf.urls.static import static
import articles.views as article_view
from django.conf import settings
from rest_framework.routers import DefaultRouter,SimpleRouter
schema_view = get_swagger_view(title='新闻系统 API')
from django.conf.urls import url
from django.views import static
from django.conf import settings


# 建立一个路由对象
router = DefaultRouter()
# 将我们的路由注册到url里
router.register('ArticleCategory', article_view.ArticleCategoryViewSet, 'ArticleCategory')
router.register('ArticleItem', article_view.ArticleItemViewSet, 'ArticleItem')
router.register('ArticleTag', article_view.ArticleTagViewSet, 'ArticleTagViewSet')
router.register('ArticleInfo', article_view.ArticleInfoListViewSet, "ArticleInfo")  # 有问题需要解决
router.register('ArticleDetail', article_view.ArticleDetailListViewSet, "ArticleDetail")  # 有问题需要解决


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    re_path('API/',schema_view,name='index'),
    # Debug =Fasle
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),

]
urlpatterns += router.urls

