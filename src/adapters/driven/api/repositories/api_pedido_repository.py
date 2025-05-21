import os
import requests
from src.adapters.data_mappers.pedido_aggregate_data_mapper import (
    PedidoAggregateDataMapper,
)
from src.core.domain.aggregates.pedido_aggregate import PedidoAggregate
from src.core.domain.entities.compra_entity import CompraEntity
from src.core.domain.repositories.pedido_repository import PedidoRepository
from src.core.helpers.enums.compra_status import CompraStatus


class ApiPedidoRepository(PedidoRepository):
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv(
            "PRODUTO_API_BASE_URL", "http://localhost:8001/dev/pedido"
        )

    def get(self, purchase_id: int) -> PedidoAggregate:
        response = requests.get(f"{self.base_url}/{purchase_id}")
        pedido = PedidoAggregateDataMapper.from_api_to_domain(response.json())
        return pedido

    def update_status(
        self, pedido_id: int, compra_status: CompraStatus
    ) -> PedidoAggregate:
        request = {
            "pedido_id": pedido_id,
            "status": compra_status.name,
        }
        response = requests.post(f"{self.base_url}/update_status", json=request)
        pedido = PedidoAggregateDataMapper.from_api_to_domain(response.json())
        return pedido
