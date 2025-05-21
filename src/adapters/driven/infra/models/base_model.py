from mongoengine import Document, DateTimeField, StringField, IntField
from datetime import datetime


class Counter(Document):
    name = StringField(required=True, unique=True)
    seq = IntField(default=0)

    meta = {"collection": "counters", "db_alias": "app-payments"}


def get_next_sequence(name):
    counter = Counter.objects(name=name).modify(upsert=True, new=True, inc__seq=1)
    return counter.seq


class BaseDocument(Document):
    meta = {"abstract": True, "db_alias": "app-payments", "collection": "payments"}

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
    deleted_at = DateTimeField(null=True)
