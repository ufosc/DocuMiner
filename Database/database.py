import os
from typing import Optional

import pymongo


class Database(object):
    """MongoDB CRUD Class """
    connection_strong = os.getenv('DB_CONNECTION_STRING')  # connect string format mongodb://[
    # username:password@]host1[:port1][,...hostN[:portN]][/[defaultauthdb][?options]]
    DATABASE = None

    @staticmethod
    def initialize(db_name: str) -> Optional[Exception]:
        """initialize Database engine """
        try:
            client = pymongo.MongoClient(Database.connection_strong)
            client.admin.command('ismaster')
            Database.DATABASE = client[db_name]
            return
        except Exception as err:
            print(str(err))
            return err

    @staticmethod
    def insert(collection: str, data: dict) -> None:
        """insert document to db """
        Database.DATABASE[collection].insert_one(data)

    @staticmethod
    def find(collection: str, query: dict) -> dict:
        """find document in db by id"""
        result = Database.DATABASE[collection].find_one(query)
        return result if result else {'message': 'data not found'}

    @staticmethod
    def update(collection: str, document_id: str, data: dict) -> Optional[Exception]:
        """update document in db"""
        try:
            Database.DATABASE[collection].update_one({'_id': document_id}, {"$set": data})

        except Exception as err:
            return err

    @staticmethod
    def delete(collection: str, document_id: str) -> Optional[Exception]:
        """delete document in db by id"""
        try:
            Database.DATABASE[collection].delete_one({'_id': document_id})
        except Exception as err:
            return err
