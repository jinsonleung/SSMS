import json

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from rest_framework import viewsets
from django.core import serializers
from persons.models import Person
from persons.serializer import PersonSerializer


# 类视图集
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


# 新增人员接口
@require_http_methods(['GET'])
def add_person(request):
    response = {}
    try:
        person = Person(
            person_name=request.GET.get('person_name'),
            deposit=request.GET.get('deposit')
        )
        person.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


# 显示所有人员接品
@require_http_methods(['GET'])
def show_persons(request):
    req = request.body
    print("==request.body==", req)
    response = {}
    try:
        persons = Person.objects.filter()   # 获取所有人员列表
        response['list'] = serializers.serialize('python', persons, ensure_ascii=False)    # 对象序列化
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response, safe=False, json_dumps_params={'ensure_ascii': False})    # 去除中文乱码


# ===使用第2种方法===
# 新增,仅接收json格式的post请求
@require_http_methods(['POST'])
def add_person_3(request):
    response = {}
    try:
        res = json.loads(request.body)  # 加载数据
        print('rest====', res)
        print('person_name:', res['person_name'])
        person = Person(
            person_name=res['person_name'],
            deposit=res['deposit']
        )
        person.save()   # 保存
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response = {'error', str(e)}
    return JsonResponse(response)








