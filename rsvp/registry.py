import requests
import json

REG_URL = "https://api.johnlewis.com/listing//v1/shared/DKRRQHJ"

class Product:
    def __init__(self, image, availability, price, title, wanted, purchased):
        self.image = image
        self.availability = availability
        self.price = price
        self.title = title
        self.wanted = wanted
        self.purchased = purchased


def get_products():
    products = []
    json = get_registry_json()
    products_json = json['products']
    for product in products_json:
        products.append(Product(
            product['image'],
            product['availabilityMessage'],
            product['priceData']['now'],
            product['title'],
            product['quantityWanted'],
            product['quantityPurchased']
        ))
    return products

def get_registry_json():
    headers = {
        'user-agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    r = requests.get(REG_URL, headers=headers)


    return json.loads(r.text)




if __name__ == "__main__":
    get_registry_json()
