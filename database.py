from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os, streamlit as st


@st.cache_resource
def db_connection():
    """connects to db"""

    db_user = st.secrets["DB_CONFIG"]["USER_NAME"]
    db_pwd = st.secrets["DB_CONFIG"]["USER_PWD"]
    db_name = st.secrets["DB_CONFIG"]["DB_NAME"]
    uri = f"mongodb+srv://{db_user}:{db_pwd}@{db_name}.vescxvi.mongodb.net/?retryWrites=true&w=majority"

    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")

    except Exception as err:
        print(err)
        st.exception(RuntimeError(err))
        st.stop()

    return client
