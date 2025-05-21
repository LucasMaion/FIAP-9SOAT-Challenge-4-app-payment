from mongoengine import ReferenceField, FloatField, IntField

from src.adapters.driven.infra.models.base_model import BaseDocument, get_next_sequence
from src.adapters.driven.infra.models.currencies import Currency
from src.adapters.driven.infra.models.payment_methods import PaymentMethod


class Payment(BaseDocument):
    meta = {"collection": "payments"}

    id = IntField(primary_key=True, default=lambda: get_next_sequence("payment_id"))
    payment_method = ReferenceField(PaymentMethod, required=True, reverse_delete_rule=2)
    currency = ReferenceField(Currency, required=True, reverse_delete_rule=2)
    value = FloatField(required=True)
    status = IntField(required=True)
    purchase = IntField(required=True)
