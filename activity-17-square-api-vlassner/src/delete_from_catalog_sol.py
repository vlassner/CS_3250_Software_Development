'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Description: Deletes an item from the Catalog of Items
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

# deletes an item from the catalog of items
id = input('id? ')
result = client.catalog.delete_catalog_object(
  object_id = id
)

if result.is_success():
  print(result.body)
elif result.is_error():
  print(result.errors)