from typing import Optional
from src.adapters.data_mappers.currency_entity_data_mapper import (
    CurrencyEntityDataMapper,
)

from src.core.domain.entities.compra_entity import PartialCompraEntity
from src.core.domain.value_objects.preco_value_object import PrecoValueObject
from src.core.helpers.enums.compra_status import CompraStatus


class CompraEntityDataMapper:
    @classmethod
    def from_api_to_domain(cls, api_response: dict):
        return PartialCompraEntity(
            id=api_response["id"],
            status=CompraStatus(api_response["status"]),
            total=PrecoValueObject(
                value=api_response["total"]["value"],
                currency=CurrencyEntityDataMapper.from_api_to_domain(
                    api_response["total"]["currency"]
                ),
            ),
            created_at=api_response["created_at"],
            updated_at=api_response["updated_at"],
            deleted_at=api_response["deleted_at"],
        )
