from src.adapters.data_mappers.pagamento_aggregate_data_mapper import (
    PagamentoAggregateDataMapper,
)
from src.adapters.data_mappers.pagamento_data_mapper import PagamentoEntityDataMapper
from src.adapters.driven.infra.models.payments import Payment
from src.core.domain.aggregates.pedido_aggregate import PedidoAggregate
from src.core.domain.entities.pagamento_entity import PartialPagamentoEntity
from src.core.domain.repositories.pagamento_repository import PagamentoRepository


class OrmPagamentoRepository(PagamentoRepository):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def create(self, payment: PartialPagamentoEntity, purchase: int) -> PedidoAggregate:
        db_item = PagamentoEntityDataMapper.from_domain_to_db(payment, purchase)
        payment = Payment(**db_item)
        payment.save()
        return PagamentoAggregateDataMapper.from_db_to_domain(payment)

    def get(self, payment_id: int) -> PedidoAggregate:
        payment = Payment.objects(id=payment_id).first()
        return PagamentoAggregateDataMapper.from_db_to_domain(payment)

    def update(self, payment: PartialPagamentoEntity, purchase: int) -> PedidoAggregate:
        db_item = PagamentoEntityDataMapper.from_domain_to_db(payment, purchase)
        payment = Payment.objects(id=db_item["id"]).first()
        if payment:
            for key, value in db_item.items():
                setattr(payment, key, value)
            payment.save()
        return PagamentoAggregateDataMapper.from_db_to_domain(payment)
