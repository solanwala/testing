import streamlit as st
import time

with st.spinner('Wait for it...'):
    time.sleep(10)
st.success('Done!')