from motor.frameworks import asyncio

import beanie_framework
from beanie_framework.services import create_item, get_item, update_item, delete_item,get_item_by_name


async def main():
    # Replace 'mongodb://localhost:27017/Osi_db' with your actual MongoDB connection string
    database_url = 'mongodb://localhost:27017/Osi_db'
    await beanie_framework.models.init_database(database_url)

    item_data = {"name": "asdf", "description": "absc", "price": 300, "stock": 200}

    # Create item
   # created_item = await create_item(item_data)
    #print(f"Created item: {created_item}")

    # Get item
    ##retrieved_item = await get_item(item_id)
    #(f"Retrieved item by id: {retrieved_item}")
    #get item by name
    searched_item_name = "asdf"  # Replace with the actual item name
    retrieved_item = await get_item_by_name(searched_item_name)

    if retrieved_item:
        print(f"Retrieved item by name '{searched_item_name}': {retrieved_item}")
    else:
        print(f"No item found with name '{searched_item_name}'.")

    # # Update item
    # updated_data = {"description": "Updated description."}
    # await update_item(item_id, updated_data)
    # updated_item = await get_item(item_id)
    # print(f"Updated item: {updated_item}")
    #
    # # Delete item
    # await delete_item(item_id)
    # print("Item deleted")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
