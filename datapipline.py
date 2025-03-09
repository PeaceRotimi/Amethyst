import pandas as pd

from pymongo import MongoClient
import json
import os


client = MongoClient("mongodb+srv://Oluwatoni:Xj9DbHNyLngvbmIL@amethyst.sjkhl.mongodb.net/?retryWrites=true&w=majority&appName=Amethyst")


db = client["houseHunter"]  
collection = db["Amethyst"] 

# with open("data/hackathon_listings_final.json", "r") as file:
#     data = json.load(file)

# if isinstance(data, list):  
#     collection.insert_many(data)
#     print("Data inserted successfully!")
# else:
#     collection.insert_one(data)
#     print("Single document inserted successfully!")

# client.close()
