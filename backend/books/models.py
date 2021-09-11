from django.db import models


# 图书类
class Books(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=30, blank=True, null=True)

    class Meta:  # 更改数据库表名称
        db_table = 'books'  # 修改表名
        verbose_name = '图书类'    # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['-name']  # 排序字段
