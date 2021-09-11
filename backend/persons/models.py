from django.db import models


# 图书类
class Person(models.Model):
    person_name = models.CharField('姓名', max_length=64, null=False)
    deposit = models.FloatField('存款')
    add_time = models.DateTimeField(auto_now_add=True)
    isDelete = models.BooleanField(default=False)

    class Meta:  # 更改数据库表名称
        db_table = 'person'  # 修改表名
        verbose_name = '人员'    # 详细名称
        verbose_name_plural = verbose_name  # 详细名称
        ordering = ['-person_name']  # 排序字段

    def __str__(self):  # 返回对象信息
        return self.person_name, self.deposit



