# Create your views here.
from django.shortcuts import render
from mongoengine import QuerySet
from pymongo.response import Response
from rest_framework.views import APIView

from mongoengineTest.models import Author
from mongoengineTest.serializer import AuthorSerializer


class InsertView(APIView):
    def post(self, request):
        name = request.data["name"]
        h_index = request.data["h_index"]
        pubs = request.data["pubs"]
        Author.objects.create(name=name, h_index=h_index, pubs=pubs)
        return Response(dict(msg="OK", code=10000))


class SelectView(APIView):
    def get(self, request):
        """
        查询数据
        :param request:
        :return:
        """
        authors = Author.objects.all()
        ser = AuthorSerializer(instance=authors, many=True)
        return Response(dict(msg="OK", code="10000", data=ser))


def index(request):
    authors: QuerySet = Author.objects.all()
    msglist = {'a', 'b', 'c'}

    context = {'msglist': msglist}
    print(authors.first().name)
    return render(request, "base.html", context)
