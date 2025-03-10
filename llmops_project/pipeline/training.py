import sys

from langchain_text_splitters import RecursiveCharacterTextSplitter

from llmops_project.database.mongo import MongoDBClient
from llmops_project.exception import LLMOpsException
from llmops_project.logger import logging
from llmops_project.constants import MONGO_DATABASE_NAME


class VectorDB:
    def __init__(self, model, database):
        self.model = model
        self.database = MongoDBClient(databaseName=MONGO_DATABASE_NAME)

    def _document_loader(self):
        try:
            self.context: str = None
            pass
        except Exception as e:
            raise LLMOpsException(e, sys)

    def _text_splitter(self, chunk_size: int, chunk_overlap: int):
        try:
            splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n", " ", ""],
                                                      chunk_size=chunk_size,
                                                      chunk_overlap=chunk_overlap,
                                                      )
            chunks = splitter.create_documents(texts=[self.context])

        except Exception as e:
            raise LLMOpsException(e, sys)

    def _embedding(self):
        try:
            # model, dimensions, api?
            pass
        except Exception as e:
            raise LLMOpsException(e, sys)

    def _evaluate():
        try:
            pass
        except Exception as e:
            raise LLMOpsException(e, sys)

    def _store():
        try:
            pass
        except Exception as e:
            raise LLMOpsException(e, sys)

    def setup(document=None):
        try:
            # Step one: document loader (csv/pdf/microsoft office)

            # Step two: text splitter (split strategy, chunk size, chunk overlap)

            # Step three: embeddings (openai/ollama/huggingface)

            # Step four: evaluate the result

            # Step five: store on database

            pass
        except Exception as e:
            raise LLMOpsException(e, sys) from e
