import pymongo
import pandas as pd
from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self, connection_string: str):
        """MongoDB se connect karne ke liye"""
        self.client = MongoClient(connection_string)
        self.db = None

    def connect(self, database_name: str):
        """Specific database se connect"""
        self.db = self.client[database_name]
        return f"Connected to database: {database_name}"

    def fetch_data(self, collection_name: str) -> pd.DataFrame:
        """Collection se data pandas DataFrame mein laao"""
        if self.db is None:
            raise ValueError("Pehle connect() call karo.")
        
        collection = self.db[collection_name]
        data = list(collection.find())
        if not data:
            return pd.DataFrame()
        
        df = pd.DataFrame(data)
        if '_id' in df.columns:
            df = df.drop(columns=['_id'])
        return df

    def insert_data(self, collection_name: str, df: pd.DataFrame):
        """DataFrame ko MongoDB collection mein save karo"""
        if self.db is None:
            raise ValueError("Pehle connect() call karo.")
        
        collection = self.db[collection_name]
        records = df.to_dict('records')
        if not records:
            return "Koi data nahi insert karna"
        
        result = collection.insert_many(records)
        return f"{len(result.inserted_ids)} records insert ho gaye"