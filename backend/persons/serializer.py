from rest_framework import serializers
from persons.models import Person


# 图书类序列货器
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person   # 序列化的对象名
        fields = '__all__'  # 序列货所有字段

