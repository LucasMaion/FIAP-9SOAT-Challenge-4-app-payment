from typing import Union
from src.adapters.data_mappers.meio_de_pagamento_data_mapper import (
    MeioDePagamentoEntityDataMapper,
)
from src.adapters.driven.infra.models.payment_methods import (
    PaymentMethod,
)  # Mongo model
from src.core.application.ports.meio_de_pagamento_query import MeioDePagamentoQuery
from src.core.domain.entities.meio_de_pagamento_entity import (
    MeioDePagamentoEntity,
    PartialMeioDePagamentoEntity,
)


class OrmMeioDePagamentoQuery(MeioDePagamentoQuery):
    def get(self, item_id: int) -> Union[MeioDePagamentoEntity, None]:
        result = PaymentMethod.objects(id=item_id).first()
        return (
            MeioDePagamentoEntityDataMapper.from_db_to_domain(result)
            if result
            else None
        )

    def get_all(self) -> list[MeioDePagamentoEntity]:
        result = PaymentMethod.objects()
        return [
            MeioDePagamentoEntityDataMapper.from_db_to_domain(res) for res in result
        ]

    def find(
        self, query_options: PartialMeioDePagamentoEntity
    ) -> list[MeioDePagamentoEntity]:
        raise NotImplementedError()
