from os import environ
import motor.motor_asyncio

from dotenv import load_dotenv
load_dotenv()

DB_URL = f"mongodb+srv://{environ['MONGODB_USER']}:{environ['MONGODB_PASSWORD']}@cluster0.2wkv6.mongodb.net/{environ['MONGODB_NAME']}?retryWrites=true&w=majority"  # noqa
client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
db = client[environ["MONGODB_NAME"]]
