from django.shortcuts import render
# Create your views here.
from django_tables2 import RequestConfig

from dtTest.models import Org
from dtTest.tables import OrgTable, SimpleTable


def people(request):
    # return render(request, 'dtTest/people.html', {'people': Org.objects.all()})
    # table = OrgTable(Org.objects.only("title"))
    table = SimpleTable(Org.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'dtTest/people.html', {'table': table})
