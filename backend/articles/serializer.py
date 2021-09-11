from rest_framework import serializers
from .models import *
from users.serilaizes import *

# 在models同级目录中创建serilaizes.py
# 这里通过控制fields内容API接口流可以展示的字段信息

# class 自定义类名Serializer(serializers.ModelSerializer):
#     # 如果原始数据字段存在主外键关系，需要将有ForeignKey的内容进行添加
#     category = 关联外键类的Serializer() # 存在外键的class的Serializer
#     class Meta:
#         model = 自定义类名对应的模型 # models.py中的模型名称
#         fields = "__all__" # 表示全部字段输出
#         fields = ('col_name_1', 'col_name_2')  # 表示serice中的字段内容输出
#         fields = ['col_name_1', 'col_name_2']  # 表示serice中的字段内容输出


# 一级分类
class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory
        fields = ["category_name"]


# 子栏目
class ArticleItemSerializer(serializers.ModelSerializer):
    item_category = ArticleCategorySerializer()

    class Meta:
        model = ArticleItem
        fields = ["item_category", "item_name"]


# Tag标签
class ArticleTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleTag
        fields = ["tag_name", "tag_slug"]  # API接口中显示的字段内容


# 全部info
class ArticleInfoSerializer(serializers.ModelSerializer):
    # 外键相关对象
    article_item = ArticleItemSerializer()
    article_author = UserSerializer()
    article_tags = ArticleTagSerializer(many=True)

    class Meta:
        model = ArticleInfo
        fields = "__all__"


# 文章detail
class ArticleContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleDetail
        fields = "__all__"

