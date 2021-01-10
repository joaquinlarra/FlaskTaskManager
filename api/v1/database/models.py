from mongoengine import Document, StringField, IntField


class Task(Document):
    task_id = IntField(db_field='id', primary_key=True)
    cmd = StringField(required=False)
    output = StringField(required=False)