import mongoengine


# Create your models here.

class Author(mongoengine.Document):
    # 指定 collection 名字
    meta = {'collection': 'a_authors'}

    _id = mongoengine.StringField(db_column='_id', max_length=30, primary_key=True)
    id = mongoengine.StringField(db_column='id', max_length=30, primary_key=False)
    name = mongoengine.StringField(db_column='name', max_length=30)
    h_index = mongoengine.IntField(db_column='h_index')
    pubs = mongoengine.ListField(db_field='pubs')
    orgs = mongoengine.ListField(db_field='orgs')
    n_pubs = mongoengine.IntField(db_field='n_pubs')
    tags = mongoengine.ListField(db_field='tags')
    n_citation = mongoengine.IntField(db_field='n_citation')

    def __str__(self):
        return "" + self.id + ":" + self.name
