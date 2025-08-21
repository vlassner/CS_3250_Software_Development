[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LrTg-GM5)
# Introduction 

[Square](https://squareup.com/) is a financial services platform aimed at small to medium-sized businesses, allowing them to accept credit card payments and use phones or tablets as payment registers for a point-of-sale (POS) system. The platform is available through an Application Programming Interface (API). Square is a component service that allows software developers to quickly build applications that require: 

* orders management, including processing of online payment transactions and invoices; 
* managing of customers, partners, and employees data; and
* managing of products catalog and inventory. 

# Setup

Create a free account and install Square's Software Development Kit (SDK) for Python using: 

```
pip3 install squareup
```

The documentation for Python's **squareup** package can be found [here](https://developer.squareup.com/docs/sdks/python). 

Next, create an [app](https://developer.squareup.com/apps) named "Hello World". You can skip the other settings when asked. Create a **config.py** file to store your sandbox access token like the following.  

```
SQUARE_ACCESS_TOKEN = <PASTE YOUR ACCESS TOKEN INSIDE QUOTES>
```

Add **config.py** to your *.gitignore*. 

Alternatively, a more secure setting would can be configured by setting up an environment variable named **SQUARE_ACCCESS_TOKEN**. However, this activity will use the **config.py** option for simplicity. 

Test the connection to the API by running [src/test_api.py](src/test_api.py). 

# Create a Catalog of Items

Use [src/create_catalog.py](src/create_catalog.py) to create a catalog containing 3 items. 

# List the Catalog

Use [src/list_catalog.py](src/list_catalog.py) to list the catalog of items. 

# Delete an Item from the Catalog

Now it is your turn! Study the [API documentation](https://developer.squareup.com/reference/square) under **Catalog** and complete the script called [src/delete_from_catalog.py](src/delete_from_catalog.py) that deletes an item from the catalog based on a given id. 