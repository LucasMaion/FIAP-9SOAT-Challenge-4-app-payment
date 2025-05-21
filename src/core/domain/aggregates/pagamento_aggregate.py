from typing import Optional
from src.core.domain.base.aggregate import AggregateRoot
from src.core.domain.entities.compra_entity import PartialCompraEntity
from src.core.domain.entities.pagamento_entity import PagamentoEntity


class PagamentoAggregate(AggregateRoot):
    payment: PagamentoEntity
    purchase: Optional[PartialCompraEntity] = None
