from mongoengine import StringField, BooleanField, IntField

from src.adapters.driven.infra.models.base_model import BaseDocument, get_next_sequence


class Currency(BaseDocument):
    meta = {"collection": "currencies"}

    id = IntField(primary_key=True, default=lambda: get_next_sequence("currency_id"))
    symbol = StringField(required=True)
    name = StringField(required=True)
    code = StringField(required=True)
    is_active = BooleanField(default=True)
