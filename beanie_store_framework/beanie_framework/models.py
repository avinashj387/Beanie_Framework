# models.py
from beanie import Document, init_beanie
from pydantic import BaseModel
import motor.motor_asyncio

class Item(BaseModel):
    name: str
    description: str
    price: int
    stock: int
class ItemDocument(Document, Item):
    class Settings:
        collection = "items"

async def init_database(database_url: str):
    client = motor.motor_asyncio.AsyncIOMotorClient(database_url)
    database = client.get_database()
    await init_beanie(database, document_models=[ItemDocument])
