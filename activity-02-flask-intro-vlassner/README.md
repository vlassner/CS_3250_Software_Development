# Overview

[Flask](https://flask.palletsprojects.com/en/3.0.x/) is a lightweight framework for building web applications using Python. It is know for its simplicity and ease of use.  Compared to other similar frameworks, like Django, Flask is easier to learn because less coding is required to write a simple web application. To demonstrate just that, this activity will guide through the steps to create a "Hello, World!" web app. 

# Instructions 

First, initialize virtual environment and install the flask package. 

```
python -m venv .venv 
.venv\Scripts\activate
pip3 install flask
```

Next, create the "app" package under **src**. 

```
mkdir src
cd src
mkdir app
cd app
```

Create a **__init__.py** file (inside app) with the following code: 

```
from flask import Flask

app = Flask('Hello World')

from app import routes
```

The "app" package initialization file imports flask and instantiates a Flask object, passing the name of the app as "Hello World".  After that, it imports the routes module, defined in **routes.py**.  

Create **routes.py** (inside app) with the following code: 

```
from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
```

The routes module is where the different URLs that the web app handles are defined as Python (view) functions.​ View functions are mapped to one or more route URLs. That's how Flask knows what logic to execute when a client requests a given URL.

The final step before running your web app is to define the **FLASK_APP** environment variable as: 

```
cd ..
set FLASK_APP=app
```

To run your web app simple do: 

```
flask run
```

You should get the following output:

```
* Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
127.0.0.1 - - [10/Jan/2024 10:05:31] "GET / HTTP/1.1" 200 -
```

You can then point your browser to http://127.0.0.1:5000. The "Hello, World!" should be displayed. 
