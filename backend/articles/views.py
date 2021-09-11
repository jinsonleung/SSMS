from rest_framework import viewsets
from .serializer import *
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters
from .myfilter import *
from rest_framework.response import Response


# 通过Views视图的方式实现数据读取和流式传输

# 文章类别
# class 定义的类别ViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = 定义的类别对应的model.objects.filter(status=1)
#     serializer_class = 定义的类别Serializer  # 用户筛选API中显示的字段内容
#     pagination_class = DataPagination  # 数据翻页的设置
#     lookup_field = "category_name"  # 搜索的字段 需要和filter对应 格式为http:xxxx/lookup_field的值
#

"""
只读方法 viewsets.ReadOnlyModelViewSet
增删改查 viewsets.ModelViewSet
"""


# API数据分页设置
class DataPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 10


# 文章类别
class ArticleCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleCategory.objects.filter(status=1)
    serializer_class = ArticleCategorySerializer  # 用户筛选API中显示的字段内容
    pagination_class = DataPagination  # 数据翻页的设置
    lookup_field = "category_name"  # 搜索的字段 需要和filter对应 格式为http:xxxx/lookup_field的值


# 文章栏目
class ArticleItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleItem.objects.filter(status=1)
    serializer_class = ArticleItemSerializer  # 用户筛选API中显示的字段内容
    pagination_class = DataPagination  # 数据翻页的设置
    lookup_field = "item_name"  # 搜索的字段 需要和filter对应 格式为http:xxxx/lookup_field的值


# 文章标签
class ArticleTagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ArticleTag.objects.filter(status=1)
    serializer_class = ArticleTagSerializer  # 用户筛选API中显示的字段内容
    pagination_class = DataPagination  # 数据翻页的设置
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 模糊查询字段使用
    search_fields = ('tag_name', 'tag_slug')  # 搜索的字段 需要和filter对应 格式为http:xxxx/?search=查查字段的值
    lookup_field = "tag_slug"  # 搜索的字段 需要和filter对应 格式为http:xxxx/lookup_field的值


"""
mixins.ListModelMixin 列表查询
mixins.RetrieveModelMixin 单个数据查询
viewsets.GenericViewSet 绑定url，可以从url中获取参数
"""


# 定义全部文章获取方式info
class ArticleInfoListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ArticleInfo.objects.filter(status=1)
    serializer_class = ArticleInfoSerializer  # 用户筛选API中显示的字段内容
    pagination_class = DataPagination  # 数据翻页的设置
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 模糊查询字段使用
    search_fields = ["article_title", "article_summary", "article_source", "province",
                     "city"]  # 搜索的字段 需要和filter对应 格式为http:xxxx/?search=查查字段的值
    ordering_fields = ('id', '-publish_date')  # 根据的字段排序
    lookup_field = "article_slug"  # 搜索的字段 需要和filter对应 格式为http:xxxx/lookup_field的值


# 定义全部文章获取方式content
class ArticleDetailListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = ArticleDetail.objects.all()
    serializer_class = ArticleContentSerializer
    pagination_class = DataPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)  # 文章过滤、查询类
    search_fields = ('detail_slug', 'detail_content')  # SearchFilter对应search_fields，对应模糊查询
    lookup_field = "detail_slug"


