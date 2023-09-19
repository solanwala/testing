import streamlit as st
import pandas as pd
import numpy as np

ff = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

ff = st.data_editor(
    ff,
    column_config={
    "Chart": st.column_config.LineChartColumn("Chart", width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,),
    
    }
)

ff
