 

Foodilicious
A Recipe Search Engine
Phase 1 Implementation 

Overview
	In this phase one we have implemented data collection through scrapping and cleaned the processed data and then indexed the recipes for better retrieval.
Milestones
  I. Scraping
  II. Preprocessing 
  III.  Indexing

Scraping

The recipes are scraped from various websites like 
●Allrecipes.com
●Foodista.com
●SpoonacularAPI
●Cookpad.com
The data is scraped in the json format. Python is used for scraping the data. BeautifulSoup, a python library, is used to scrap the data out of HTML. Other necessary libraries are imported, and the recipes are scrapped.

AllRecipe.com
The below snippets are used to scrape all the recipe links, then using the API key of spoonacular, the data is obtained in json and written in the output file respectively.




Foodista.com :
The whole HTML page data is scraped with the below code:

There were several pages of recipes on this website. To get each recipe from a page, the below snippet of code is used:

The output will have the relative path of all recipes in that page. To get the available page links, below code is used:

The output consists of a tag along with href containing the link to the pages available. From the output, the href link is taken so that we can scrape data from those available pages.
The recipe links are given to Spoonacular API “Extract Recipe from Website” so as to get the necessary recipe information in the form of json.


Spoonacular API:
	There are several cuisines under which all the recipes reside. Some cuisine names are Indian, African, American and Mexican. Using these cuisine names, the recipes are scraped through the API provided by Spoonacular. There are two different APIs used for this purpose.
●Search API - The parameter includes cuisine name and returns all the recipes belonging to that cuisine.

The output of this API will have the list of recipe IDs along with their title, source URL, image and image type for every cuisine. The Ids of these recipes will be given to the next API to get the particular recipe.
●Extract Recipe by ID - Extracts recipe with the given ID.
The recipe IDs are taken from the output of Search API of a particular cuisine and the whole recipe is taken with the other API.

Similarly cookpad website is also scraped,The recipes are then written to the output file to get processed.

Preprocessing 
An image of the recipe before preprocessing is shown below(raw data). 


Preprocessing is done in two main stages. 
●In the first stage duplicate data in the same website is removed.

The variable data will have the data from the output file of the previous stage. Since it is a list, to remove duplicates, set functionality is used.
●In the second stage, only a few terms are picked for categorization such as ingredients list including the amount and unit, recipe name, vegetarian, gluten free, serving, cooking time, health score, aggregate likes, recipe site.
●As the final step, the incomplete recipes(those without title or ingredients) are not taken for the next stage. An image of the recipe after preprocessing is shown below.

The actual data in json format will have the ingredients in the extendedIngredients field. The necessary ingredients data like name, amount and unit(Eg: olive oil, tbsp and 4) are fetched from that field; rest are discarded. The preprocessed recipe looks like the below snippet.


Indexing
	For Indexing elastic search is used. Elasticsearch is a distributed, free and open source and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. Elasticsearch is built on Apache Lucene. It is known for its simple REST APIs, distributed nature, speed, and scalability.
	Elastic search server is started which runs at the port 9200 of localhost. Elasticsearch client library for python is used to do indexing with elastic search through python. The input files are fed as a json list through the helper function which indexes each of the given json(single recipe) separately and stores them. We can view the indexes of the file through http://127.0.0.1:9200/_all.
