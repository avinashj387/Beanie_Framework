# services.py
from beanie_framework.models import ItemDocument

async def create_item(item_data):
    item = ItemDocument(**item_data)
    await item.insert()
    return item

async def get_item_by_name(item_name):
    # Use Beanie's find_one method to retrieve an item by its name
    item = await ItemDocument.find_one({"name": item_name})
    return item
async def get_item(item_id):
    item = await ItemDocument.get(item_id)
    return item

async def update_item(item_id, updated_data):
    item = await ItemDocument.get(item_id)
    for key, value in updated_data.items():
        setattr(item, key, value)
    await item.update()

async def delete_item(item_id):
    item = await ItemDocument.get(item_id)
    await item.delete()
