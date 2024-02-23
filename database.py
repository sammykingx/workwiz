from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os, streamlit as st


load_dotenv()

@st.cache_resource
def db_connection():
    """connects to db"""

    password = os.getenv("USER_PWD")
    uri = f"mongodb+srv://workwiz_admin:{password}@workwizdb.vescxvi.mongodb.net/?retryWrites=true&w=majority"

    # Create a new client and connect to the server
    #client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

    except Exception as err:
        print(err)
        st.exception(RuntimeError(err))
        st.stop()

    return client
