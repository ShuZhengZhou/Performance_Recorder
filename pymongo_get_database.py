from pymongo import MongoClient
from pymongo.server_api import ServerApi
from connection_string import URI
def get_database():
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(URI, server_api=ServerApi('1'))
   
   try:
      client.admin.command('ping')
      print("Pinged your deployment. You successfully connected to MongoDB!")
   except Exception as e:
      print("Connection failed, error message:")
      print(e)

   database = client["test"]
   return database["Performance_Recorder"]

# This code will only run if this script is not imported as module
if __name__ == "__main__":
   dbname = get_database()



