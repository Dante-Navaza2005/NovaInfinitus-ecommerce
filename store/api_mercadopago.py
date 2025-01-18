import mercadopago
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta, timezone

load_dotenv()


mercado_public_key = os.getenv('mercado_public_key')
mercado_access_token = os.getenv('mercado_access_token')


def create_payment(items_ordered, link):
    # Configure suas credenciais
    sdk = mercadopago.SDK(mercado_access_token)  # Validando access token

    # Items que o usuário está comprando
    items = []
    for item in items_ordered:
        quantity = int(item.quantity)
        product_name = item.itemstock.product.name
        unit_price = float(item.itemstock.product.price)
        items.append({
            "title": product_name,
            "quantity": quantity,
            "unit_price": unit_price
        })

    # Calcular a data de expiração (1 hora a partir do horário atual)
    now_utc = datetime.now(timezone.utc)
    expiration_time = now_utc + timedelta(hours=1)# Adicionar 1 hora
    expiration_iso = expiration_time.isoformat(timespec='milliseconds')  # Formatar em ISO 8601


    # Criar os dados de preferência
    preference_data = {
        "items": items,
        "auto_return": "all",  # Retorno automático para o site após pagamento
        "back_urls": {  # Links que serão carregados em cada cenário de pagamento
            "success": link,
            "failure": link,
            "pending": link,
        },
        "expires": True,
        "expiration_date_to": expiration_iso  # Adicionando a data de expiração
    }

    # Criar uma preferência
    preference_response = sdk.preference().create(preference_data)  # Criando requisição com várias informações sobre o pagamento
    
    payment_link = preference_response["response"]["init_point"]
    payment_id = preference_response["response"]["id"]  # Obtendo o ID do pagamento para tratá-lo
    return payment_link, payment_id
