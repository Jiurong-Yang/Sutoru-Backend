from pprint import pprint
from square import Square
from square.environment import SquareEnvironment

client = Square(
    environment=SquareEnvironment.PRODUCTION,
    token="EAAAl986zWpPse2sD_jxSp_66sdG7cBTp_38HuOv01eIXTyw6qtbE5wSHpozbzMm"
)

print(client.catalog.list())
#pprint(client.locations.list())
"""
client.orders.create(
    idempotency_key="0c75287f-ac3d-4bae-b90d-598f558b2216",
    order={
        "location_id": "LK41MJ92QWKTX",
        "customer_id": "test",
        "taxes": [],
        "line_items": [
            {
                "quantity": "1",
                "catalog_object_id": "b6d35454-d7bd-4f68-a009-b0413a83761f",
                "item_type": "ITEM",
                "base_price_money": {
                    "amount": 50,
                    "currency": "USD"
                }
            }
        ]
    }
)
"""
print("Success!")