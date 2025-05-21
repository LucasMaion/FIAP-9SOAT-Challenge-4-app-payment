from mongoengine import StringField, BooleanField, IntField

from src.adapters.driven.infra.models.base_model import BaseDocument, get_next_sequence


class PaymentMethod(BaseDocument):
    meta = {"collection": "payment_methods"}

    id = IntField(
        primary_key=True, default=lambda: get_next_sequence("payment_method_id")
    )
    name = StringField(required=True)
    sys_name = StringField(required=True)
    internal_comm_method_name = StringField(null=True)
    internal_comm_delay = IntField(null=True)
    description = StringField(null=True)
    is_active = BooleanField(default=True)
