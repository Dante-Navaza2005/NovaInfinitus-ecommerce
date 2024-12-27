import mercadopago
from dotenv import load_dotenv
import os

load_dotenv()


public_key = os.getenv('mercado_public_key')
access_token = os.getenv('mercado_access_token')

def create_payment(items_ordered, link) :
    #configure your credentials
    sdk = mercadopago.SDK(access_token) #? validating access token

    #? items the user is purchasing
    items = []
    for item in items_ordered :
        quantity = int(item.quantity)
        product_name = item.itemstock.product.name
        unit_price = float(item.itemstock.product.price)
        items.append({
            "title": product_name, 
            "quantity": quantity, 
            "unit_price": unit_price
            })

    # Create items in the preference. preference = personalized charge for clients
    preference_data = {
        "items": items,
        "auto_return": "all", #? auto-return to site after payment  
        "back_urls": { #? links that will be loaded in each payment cenario
            "success": link,
            "failure": link,
            "pending": link,
        }, 
    }

    # Create a preference
    preference_response = sdk.preference().create(preference_data) #? creating request with various informations about the payment
    payment_link = preference_response["response"]["init_point"]
    payment_id = preference_response["response"]["id"] #? obtaining the payment id to treat it
    return payment_link, payment_id