from mongoengine import ReferenceField, StringField, IntField

from src.adapters.driven.infra.models.base_model import BaseDocument, get_next_sequence
from src.adapters.driven.infra.models.payments import Payment


class PaymentMetadata(BaseDocument):
    meta = {"collection": "payment_metadata"}

    id = IntField(
        primary_key=True, default=lambda: get_next_sequence("payment_metadata_id")
    )
    provider_transaction_id = StringField(required=True)
    payment = ReferenceField(Payment, unique=True, null=True, reverse_delete_rule=2)
