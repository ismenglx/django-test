# Create your views here.
from django.shortcuts import render
from mongoengine import QuerySet
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets

import mongoengineTest
from mongoengineTest.models import Author
from mongoengineTest.serializer import AuthorSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    继承 ModelViewSet，需要给 serializer_class、queryset 两个属性赋值
    """
    serializer_class = AuthorSerializer
    queryset: QuerySet = Author.objects.all()

    # permission_classes = permissions.IsAuthenticatedOrReadOnly

    # URL：http://127.0.0.1:8000/author/all/ 默认使用 list 方法
    def list(self, request, *args, **kwargs):
        ser = AuthorSerializer(instance=self.queryset, many=True)
        # print(ser.data)
        return Response(ser.data)

    # url: http://127.0.0.1:8000/author/all/retreive/?name=XXX
    def retrieve(self, request, *args, **kwargs):
        name = request.query_params.get(key='name')
        # name 为空或查不到该数据
        if name is None | self.queryset.get(name=name) is None:
            ser = AuthorSerializer(self.queryset.first())
        else:
            ser = AuthorSerializer(self.queryset.get(name=name))
        return Response(ser.data)


def index(request):
    authors = Author.objects.all()
    msglist = {'a', 'b', 'c'}

    context = {'msglist': msglist}

    # 测试
    mongoengineTest.util.select.test()
    return render(request, "base.html", context)
