import streamlit as st
import pandas as pd
import numpy as np

ff = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

ff = st.data_editor(
    ff,
    column_config={
    "Chart": st.column_config.LineChartColumn("Chart", "help": "something"),
    
    }
)

ff
