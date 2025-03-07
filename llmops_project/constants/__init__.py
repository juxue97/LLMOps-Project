import os

MONGO_CONNETION_URL = os.getenv(
    "MONGO_CONNETION_URL", "mongodb://root:rootpass@192.168.1.7:27017/?authSource=admin")

MONGO_DATABASE_NAME = os.getenv(
    "MONGO_DATABASE_NAME", "LLMOps"
)
