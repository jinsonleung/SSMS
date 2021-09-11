from datetime import timezone
from django.db import models

# 「Django 框架模板」新闻行业资讯数据后端API接口开发模板
# https://zhuanlan.zhihu.com/p/363757925


class User(models.Model):
    name = models.CharField(max_length=20)
    ArticleItemAddUser = models.CharField(max_length=20)


# 根据你的实际情况进行编辑设置对应表单、和业务模型。
# 文章类别管理
class ArticleCategory(models.Model):
    category_name = models.CharField(max_length=20, verbose_name='文章类别名称', help_text="文章类别名称")
    StatusChoices = (("1", "在用"), ("0", "未用"))
    status = models.CharField(choices=StatusChoices, max_length=1, default=1, verbose_name='使用状态',help_text="使用状态")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    add_user = models.ForeignKey(User, related_name='ArticleCategoryAddUser', on_delete=models.CASCADE, verbose_name='创建用户', help_text="创建用户")

    class Meta:
        verbose_name = '文章类别管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


# 文章栏目管理
class ArticleItem(models.Model):
    item_category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, related_name='ArticleItemCategory', verbose_name="文章类别", help_text="文章类别")
    item_name = models.CharField(max_length=20, verbose_name="栏目名称", help_text="栏目名称")
    StatusChoices = (("1", "在用"), ("0", "未用"))
    status = models.CharField(choices=StatusChoices, max_length=1, default=1, verbose_name='使用状态', help_text="使用状态")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    add_user = models.ForeignKey(User, related_name='ArticleItemAddUser', on_delete=models.CASCADE, verbose_name='创建用户', help_text="创建用户")

    class Meta:
        verbose_name = '文章栏目管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item_name


# 文章标签管理
class ArticleTag(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name='标签名称', help_text="标签名称")
    tag_slug = models.SlugField(max_length=50, verbose_name="标签slug", help_text='填写英文、字母、下划线、数字，不可重复', unique=True)
    StatusChoices = (("1", "在用"), ("0", "未用"))
    status = models.CharField(choices=StatusChoices, max_length=1, default=1, verbose_name='使用状态',
                              help_text="使用状态")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    add_user = models.ForeignKey(User, related_name='ArticleTagAddUser', on_delete=models.CASCADE, verbose_name='创建用户', help_text="创建用户")

    class Meta:
        verbose_name = '文章标签管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.tag_name


# 文章内容管理
class ArticleInfo(models.Model):
    article_title = models.CharField(max_length=50, default="", verbose_name='新闻标题', help_text="新闻标题")
    article_item = models.ForeignKey(ArticleItem, related_name='ArticleInfoItem', on_delete=models.CASCADE, verbose_name='文章栏目', help_text="文章栏目")
    ai_type = models.CharField(max_length=20, verbose_name='AI分类', help_text="AI分类")
    article_summary = models.TextField(verbose_name='文章摘要', help_text="文章摘要")
    article_source = models.CharField(max_length=100, default="", verbose_name='文章来源', help_text="文章来源")
    article_key_words = models.CharField(max_length=300, default="", verbose_name='文章关键词', help_text="文章关键词", blank=True)
    article_slug = models.SlugField(default="日期+ID的格式", verbose_name='文章slug', help_text="文章slug", primary_key=True)
    article_author = models.ForeignKey(User, related_name='ArticleInfoAuthor', on_delete=models.CASCADE, verbose_name='文章作者', help_text="文章作者", null=True, blank=True)
    article_tags = models.ManyToManyField(ArticleTag, related_name='ArticleInfoTags', verbose_name='文章标签', help_text="文章标签", null=True, blank=True)
    article_publish_date = models.DateTimeField(auto_now_add=True, verbose_name='文章发布日期', help_text="文章发布日期")
    article_cover_1 = models.ImageField(upload_to='Article_Cover/%Y/%m', default='Article_Cover/default.png', verbose_name='文章自定义封面', help_text="文章自定义封面", null=True, blank=True)
    article_cover_2 = models.TextField(default="原创", verbose_name="文章原文封面图片链接", help_text="文章原文封面图片链接", null=True, blank=True)
    article_url = models.TextField(default="原创", verbose_name="文章原文链接", help_text="文章原文链接", null=True, blank=True)
    article_video_url = models.TextField(default="原创", verbose_name="文章视频链接", help_text="文章视频链接", null=True, blank=True)
    province = models.CharField(max_length=20, verbose_name='省市', help_text="省市")
    city = models.CharField(max_length=20, verbose_name='城市', help_text="城市")
    praise_num = models.IntegerField(default=0, verbose_name='点赞数', help_text="点赞数")
    read_num = models.IntegerField(default=0, verbose_name='浏览数', help_text="浏览数")
    fav_num = models.IntegerField(default=0, verbose_name='收藏数', help_text="收藏数")
    StatusChoices = (("0", "未审核"), ("1", "已审核"), ("2", "审核不通过"))
    status = models.CharField(choices=StatusChoices, max_length=1, default=0, verbose_name='审核状态', help_text="审核状态")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    class Meta:
        verbose_name = '新闻基础信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_title


# 文章详情管理
class ArticleDetail(models.Model):
    detail_slug = models.SlugField(default="日期+ID的格式", verbose_name='文章slug', help_text="文章slug", primary_key=True)
    detail_content = models.TextField('内容正文', default='', null=True, blank=True)

    class Meta:
        verbose_name = '文章详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.detail_slug


# 文章基础信息和详情拼接
class Articles(ArticleInfo, ArticleDetail):
    class Meta:
        verbose_name = '新闻编辑内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article_title

