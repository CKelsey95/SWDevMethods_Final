from flask import Flask, render_template 
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# RUN WITH flask --debug run
# This will reload the server every time you save

# MONGO CONNECTION
load_dotenv()
MONGOAPIKEY = os.getenv('MONGO_DB_API_KEY')

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = MONGOAPIKEY

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


# ROUTES

app = Flask(__name__)

# HOME ROUTE
@app.route("/")
def index():

    #PASS VARIABLES HERE 
    return render_template('index.html', title='Home', page_title='Welcome to the Home Page')

 
if __name__ == '__main__':
    app.run(debug=True)
