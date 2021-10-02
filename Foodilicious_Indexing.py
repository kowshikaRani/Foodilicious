# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 18:16:21 2021

@author: kavitha and kowshika
"""

# Necessary imports
import json
from time import sleep
from elasticsearch import Elasticsearch, helpers # Client for elastic search

# Creating a instance
client = Elasticsearch("localhost:9200")

file_allRecipe = open("E:/sem9/Information Retrievel/Search_Engine Project/PreprocessedallRecipe.txt","rb+")
file_foodista = open("E:/sem9/Information Retrievel/Search_Engine Project/PreprocessedFoodista.txt","rb+")
file_spoonacular = open("E:/sem9/Information Retrievel/Search_Engine Project/PreprocessedSpoonacular.txt","r+", encoding="utf8")

data_allRecipe = file_allRecipe.readlines()
data_foodista = file_foodista.readlines()
data_spoonacular = file_spoonacular.readlines()

# Converting the file data to a list of json(each json is a recipe)
doc_list=[]
def convert_data_json(data):
    global doc_list
    for dat in data:
        dat = dat.replace("True", "true")
        dat = dat.replace("False", "false")
        # Converting single quote to double quote
        print(dat)
    
        dict_doc = json.loads(dat)
        print(dict_doc)
        
        try:
          doc_list += [dict_doc]
        
        except json.decoder.JSONDecodeError as err:
          print ("ERROR for num = ", err.pos, "-- JSONDecodeError = ", err, "for doc = ", err.doc)

convert_data_json(data_allRecipe)
convert_data_json(data_foodista)
convert_data_json(data_spoonacular)

print ("Dict docs length = ", len(doc_list))

# Indexing the data in list using helper API

try:
  resp = helpers.bulk(
  client,
  doc_list,
  index = "some_index",
  doc_type = "_doc"
  )
  print ("helpers.bulk() RESPONSE:", resp)
  print ("helpers.bulk() RESPONSE:", json.dumps(resp, indent=4))

except Exception as err:
  print("Elasticsearch helpers.bulk() ERROR:", err)
  quit()
  

# Querying to see if the data is indexed properly  
query_all = {
'size' : 10000,
'query': {
'match_all' : {}
}
}

print ("Sleeping for a two seconds to wait for indexing request to finish.")
sleep(2)

# pass the query_all dict to search() method
resp = client.search(
index = "some_index",
body = query_all
)

print ("search() response:", json.dumps(resp, indent=4))

# print the number of docs in index
print ("Length of docs returned by search():", len(resp['hits']['hits']))