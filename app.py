import streamlit as st

from streamlit.connections import SQLConnection
conn = st.experimental_connection("my_sql_connection", type=SQLConnection)

