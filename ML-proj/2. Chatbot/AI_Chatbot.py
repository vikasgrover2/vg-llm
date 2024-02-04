from openai import OpenAI
import os
import pandas as pd
import psycopg2
import psycopg2.pool
import psycopg2.extras
import warnings
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool
import streamlit as st
import random

warnings.filterwarnings('ignore')
postgres_username = os.environ['POSTGRES_USER']
postgres_password = os.environ['POSTGRES_PASSWORD']
postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_CONTAINER_PORT']
postgres_database = os.environ['POSTGRES_DB']
conn_str = f'postgresql://{postgres_username}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_database}'
PgresEngine = create_engine(conn_str, pool_size=5)

def getconn():   
    c= PgresEngine.connect()
    return c

def closeconn(c):
    c.close()

def closepool():
    PgresEngine.dispose()  

def get_data_from_db(sql):
    postgres_connection = getconn()
    df = pd.read_sql_query(sql=sql,con=postgres_connection)
    closeconn(postgres_connection)
    return df

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

dataf = pd.DataFrame(data)
st.title("FOR EX\:GPT4")
schemaname = 'dbt_snapshots'
tablename = 'fta_weekly_snapshot'
data = get_data_from_db(f"Select * from {schemaname}.{tablename}")
colums = ','.join(data.columns)

@st.cache_resource
def add_to_df(num):
    global dataf
    dataf = dataf + num
    return dataf

def chat_actions():
    global dataf
    st.session_state["chat_history"].append(
        {"role": "user", "content": st.session_state["chat_input"]},
    )
    if "chat_history" in st.session_state and "human_name" not in st.session_state:
        st.session_state.human_name = st.session_state["chat_input"]
        st.session_state["chat_history"].append(
                {
                    "role": "assistant",
                    "content": f'Nice to meet you {st.session_state.human_name}. How can I help you today?',
                },  
            )
    else:
        st.session_state.dataframe = True       
        st.session_state["chat_history"].append(
                {"role": "assistant",
                    "content": f'Is there anything else I can help with?',
                },  
            )

if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
        st.session_state["chat_history"].append(
            {"role": "assistant",
                "content": "Hello. I am your personal data analyst!",
            }, 
        )
        st.session_state["chat_history"].append(
            {"role": "assistant",
                "content": "May I know who do I have the pleasure of working with today?",
            }, 
        )
    
#st.chat_input("Enter your message", on_submit=chat_actions, key="chat_input")
with st.container():
    for i in st.session_state["chat_history"]:
            with st.chat_message(name=i["role"]):
                st.write(i["content"])
                
with st.container():
    st.text_input("Enter your message", on_change=chat_actions, key="chat_input")
    
with st.sidebar:
    st.dataframe(add_to_df(random.randint(1, 10)*2))
    #if "dataframe" in st.session_state:
    #st.write(st.session_state)
    