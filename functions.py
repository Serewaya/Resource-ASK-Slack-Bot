import pymongo
from pymongo import MongoClient 
import os

#Main Database
cluster=MongoClient("mongodb+srv://projectask:wD4odl0AK8ahUmFc@cluster0.e0sdb.mongodb.net/discord?retryWrites=true&w=majority")
db = cluster["discord"]
collection = db["id"]
def blurb_format(initial):
    blurb = ""
    count = 0
    for letter in initial:
        count+=1
        blurb+=letter
        if count>70 and letter==" ":
            blurb+="\n"
            count=0
    return blurb



def return_database(arr):
    keys = ['link', 'category', 'expiration', 'area', 'gender']
    content_dict = dict(zip(keys, arr))
    emptyed = content_dict.copy()
    for value in content_dict:
        if content_dict[value] == "none":
            del emptyed[value]
    results = collection.find(emptyed)
    return results