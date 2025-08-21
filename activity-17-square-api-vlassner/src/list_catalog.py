'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: Lists the Catalog of Items
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

# lists the catalog of items
result = client.catalog.list_catalog(
  types = "item"
)

if result.is_success():
  items = result.body['objects']
  for item in items: 
    print(f"{item['id']}, {item['created_at']}, {item['item_data']['name']}")
elif result.is_error():
  print(result.errors)
