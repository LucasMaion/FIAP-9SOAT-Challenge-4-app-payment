# Create currency
from src.adapters.driven.infra.models.currencies import Currency
from src.adapters.driven.infra.models.payment_methods import PaymentMethod
from src.adapters.driven.infra.models.payments import Payment


def seed_db():
    currency = Currency(
        symbol="R$", name="Brazilian Real", code="BRL", is_active=True
    ).save()

    # Create payment method
    payment_method = PaymentMethod(
        name="Mercado Pago QR Code",
        sys_name="DefaultPaymentProvider",
        internal_comm_method_name="PaymentEvent.internal_finalize_payment",
        internal_comm_delay=5,
        description="Pagamento para processar pelo mercado pago, cliente escaneia o QR Code para realizar transação.",
        is_active=True,
    ).save()

    # Create payment
    payment = Payment(
        payment_method=payment_method,
        currency=currency,
        value=100,
        status=1,
        purchase=1,
    ).save()

    # Create payment
    payment = Payment(
        payment_method=payment_method,
        currency=currency,
        value=200,
        status=1,
        purchase=2,
    ).save()

    # Create payment
    payment = Payment(
        payment_method=payment_method,
        currency=currency,
        value=300,
        status=1,
        purchase=1,
    ).save()

    print("Seed data inserted successfully.")
