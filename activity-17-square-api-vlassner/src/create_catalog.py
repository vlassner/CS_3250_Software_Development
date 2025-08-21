'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: Creates the Catalog of Items
'''

from square.client import Client
import os, uuid, sys
from config import SQUARE_ACCESS_TOKEN

client = Client(
    access_token=SQUARE_ACCESS_TOKEN,
    environment='sandbox')

result = client.locations.list_locations()

if result.is_error():
  sys.exit(1)

# creates the catalog
items = [ { 'code':'door-001' }, { 'code':'door-002' }, { 'code':'window-001' } ]
seq = 1
for item in items: 
  result = client.catalog.upsert_catalog_object(
    body = {
      "idempotency_key": str(uuid.uuid4()),
      "object": {
        "type": "ITEM",
        "id": f"#{seq}",
        "item_data": {
          "name": item['code'],
          "description": "",
          "variations": [
              {
                  "type": "ITEM_VARIATION",
                  "id": "#Small",
                  "item_variation_data": {
                      "item_id": f"#{seq}",
                      "name": "Small",
                      "pricing_type": "VARIABLE_PRICING"
                  }
              }
          ]
        }
      }
    }
  )
  if result.is_error():
    print(result.errors)
  else:
    seq += 1

print('done!')