"""
表格展示内容类
"""
import itertools

import django_tables2 as tables
from django.db.models.functions import Length

from dtTest.models import Org


class OrgTable(tables.Table):
    class Meta:
        model = Org
        template_name = 'django_tables2/bootstrap.html'


class SimpleTable(tables.Table):
    """
    SimpleTable 类实现自定义 django_tables2 展示表格式
    """

    class Meta:
        model = Org
        sequence = ('id', 'title')

    # row_number = tables.Column(empty_values=())
    id = tables.Column(visible=False)
    title = tables.Column()

    # id = tables.Column()
    # age = tables.Column()

    def __init__(self, *args, **kwargs):
        super(SimpleTable, self).__init__(*args, **kwargs)
        self.counter = itertools.count()

    # TODO 根据 title 字段长度 排序
    def order_title(self, QuerySet, is_descending):
        QuerySet = QuerySet.annotate(
            length=Length('title')).order_by(('-' if is_descending else '') + 'length')
        return QuerySet, True

    # def render_row_number(self):
    #     return 'Row %d' % next(self.counter)

    def render_id(self, value):
        return '<%s>' % value
