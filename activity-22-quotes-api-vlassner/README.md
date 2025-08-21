# Overview

The goal of this activity is to demonstrate how to implement an API in Python using a library package called [FastAPI](https://fastapi.tiangolo.com/). The API to be developed returns a random quote based on [Kaggle's Quotes Dataset](https://www.kaggle.com/datasets/akmittal/quotes-dataset).

# Steps

## Step 1 - Virtual Environment

Create a virtual environment and install all of the required packages from **requirements.txt**. 

## Step 2 - API Specification

Open [quotes.yaml](quotes.yaml) which is a description of the quotes API in [OpenAPI](https://swagger.io/specification/). 

## Step 3 - Code Generator

Run the following to generate the initial code of the API. 

```
.venv/bin/fastapi-codegen --input quotes.yaml --output src
```

## Step 4 - Modify Main

Modify **main.py** by adding the following import statements. 

```
from fastapi import Response
import random
```

Add the hard-coded quotes list below. 

```
quotes = [
  {
    "Id": 1,   
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss",
    "Tags": [
      "attributed-no-source",
      "cry",
      "crying",
      "experience",
      "happiness",
      "joy",
      "life",
      "misattributed-dr-seuss",
      "optimism",
      "sadness",
      "smile",
      "smiling "
    ],
    "Popularity": 0.15566615566615566,
    "Category": "life"
  },
  {
    "Id": 2,   
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss",
    "Tags": [
      "attributed-no-source",
      "cry",
      "crying",
      "experience",
      "happiness",
      "joy",
      "life",
      "misattributed-dr-seuss",
      "optimism",
      "sadness",
      "smile",
      "smiling "
    ],
    "Popularity": 0.15566615566615566,
    "Category": "happiness"
  },
  {
    "Id": 3,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "love"
  },
  {
    "Id": 4,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "life"
  },
  {
    "Id": 5,   
    "Quote":
      "I'm selfish, impatient and a little insecure. I make mistakes, I am out of control and at times hard to handle. But if you can't handle me at my worst, then you sure as hell don't deserve me at my best.",
    "Author": "Marilyn Monroe",
    "Tags": [
      "attributed-no-source",
      "best",
      "life",
      "love",
      "mistakes",
      "out-of-control",
      "truth",
      "worst "
    ],
    "Popularity": 0.12912212912212911,
    "Category": "truth"
  },
  {
    "Id": 6,   
    "Quote": "Be yourself; everyone else is already taken.",
    "Author": "Oscar Wilde",
    "Tags": [
      "attributed-no-source",
      "be-yourself",
      "honesty",
      "inspirational",
      "misattributed-oscar-wilde "
    ],
    "Popularity": 0.11322311322311322,
    "Category": "inspiration"
  },
  {
    "Id": 7,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "humor"
  },
  {
    "Id": 8,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "philosophy"
  },
  {
    "Id": 9,   
    "Quote":
      "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe.",
    "Author": "Albert Einstein",
    "Tags": [
      "attributed-no-source",
      "human-nature",
      "humor",
      "infinity",
      "philosophy",
      "science",
      "stupidity",
      "universe "
    ],
    "Popularity": 0.10312710312710313,
    "Category": "science"
  },
  {
    "Id": 10,   
    "Quote":
      "Be who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.",
    "Author": "Bernard M. Baruch",
    "Tags": [
      "ataraxy",
      "be-yourself",
      "confidence",
      "fitting-in",
      "individuality",
      "those-who-matter "
    ],
    "Popularity": 0.10189010189010189,
    "Category": ""
  }]
```

Finally, replace **get_quote_0**'s implementation with the following. 

```
@app.get('/quotes/0', response_model=Quote)
def get_quotes_0(response: Response) -> Quote:
    """
    Returns a random quote
    """
    response.status_code = 200
    raw_json = quotes[random.randint(0, len(quotes))]
    quote = Quote(
        id=raw_json['Id'], 
        text=raw_json['Quote'], 
        author=raw_json['Author'], 
        category=raw_json['Category'],
        popularity=raw_json['Popularity'],
        tags=raw_json['Tags'])
    return quote
```

# Test & Validation

Run the following to start the API server. 

```
.venv/bin/uvicorn src.main:app
```

Try opening the page [http://127.0.0.1:8000/quotes/0](http://127.0.0.1:8000/quotes/0).

Write **client.py** using the following.

```
# client.py
import requests
API_URL = 'http://127.0.0.1:8000'
url = '{}{}'.format(API_URL, '/quotes/0')
response = requests.get(
    url, 
    headers = { }, 
    params = { }
)
if response.status_code == 200:
    print(response.json())
else:
    raise Exception("Invalid Request! Check your API's documentation!\n" + response.text)        
```