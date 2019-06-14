import mongoengine
"""
MongoDB 数据库，配置在 settings.py 文件中：
    db='test', host='192.168.1.123', port=27017
    Author 类
"""


class Author(mongoengine.Document):
    # 指定 collection 名字
    meta = {'collection': 'a_authors'}

    # _id = mongoengine.StringField(db_column='_id', max_length=30, primary_key=True)
    id = mongoengine.StringField(db_column='id', max_length=30, primary_key=True)
    name = mongoengine.StringField(db_column='name', max_length=30)
    h_index = mongoengine.IntField(db_column='h_index')
    """
     "pubs": [
            {
                "i": "55a6921a65ce054aad6c1a31",
                "r": 2
            }
        ]
        
    pubs 字段是 Array 类型，每个元素又是个 Document
    """
    pubs = mongoengine.ListField(db_field='pubs')
    orgs = mongoengine.ListField(db_field='orgs')
    n_pubs = mongoengine.IntField(db_field='n_pubs')
    tags = mongoengine.ListField(db_field='tags')
    n_citation = mongoengine.IntField(db_field='n_citation')

    def __str__(self):
        return "" + self.id + ":" + self.name
