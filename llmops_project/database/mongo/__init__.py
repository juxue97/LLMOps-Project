from pymongo import MongoClient
import sys

from llmops_project.constants import MONGO_CONNETION_URL
from llmops_project.logger import logging
from llmops_project.exception import LLMOpsException

# Encrypt the data transmit between program and db (TSL)
# ca = certifi.where()


class MongoDBClient:
    client = None

    def __init__(self, databaseName: str):
        try:
            if MongoDBClient.client is None:
                mongoDBUrl = MONGO_CONNETION_URL
                if mongoDBUrl is None:
                    raise Exception(
                        "Environment key: MONGO_CONNETION_URL is not set")
                MongoDBClient.client = MongoClient(host=mongoDBUrl)

            self.client = MongoDBClient.client
            self.database = self.client[databaseName]
            logging.info("MongoDB connection successful")

        except Exception as e:
            raise LLMOpsException(e, sys) from e
