from rest_framework import serializers
from books.models import Books


# 图书类序列货器
class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段