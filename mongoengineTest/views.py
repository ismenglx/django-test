# Create your views here.
from django.shortcuts import render
from mongoengine import QuerySet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_mongoengine import viewsets

from mongoengineTest.models import Author
from mongoengineTest.serializer import AuthorSerializer


class InsertView(APIView):
    def post(self, request):
        name = request.data["name"]
        h_index = request.data["h_index"]
        pubs = request.data["pubs"]
        Author.objects.create(name=name, h_index=h_index, pubs=pubs)
        return Response(dict(msg="OK", code=10000))


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset: QuerySet = Author.objects.all()

    # permission_classes = permissions.IsAuthenticatedOrReadOnly

    def list(self, request, *args, **kwargs):
        queryset = Author.objects.all()
        ser = AuthorSerializer(instance=queryset, many=True)
        # print(ser.data)
        return Response(ser.data)

    def retrieve(self, request, *args, **kwargs):
        ser = AuthorSerializer(self.queryset.first())
        return Response(ser.data)


def index(request):
    authors = Author.objects.all()
    msglist = {'a', 'b', 'c'}

    context = {'msglist': msglist}
    print(authors.first().name)
    return render(request, "base.html", context)
