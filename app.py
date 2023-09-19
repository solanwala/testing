import streamlit as st
import pandas as pd
import numpy as np

ff = pd.DataFrame(
    {
        "sales": [
            [0, 4, 26, 80, 100, 40],
            [80, 20, 80, 35, 40, 100],
            [10, 20, 80, 80, 70, 0],
            [10, 100, 20, 100, 30, 100],
        ],
    })

st.data_editor(
    ff,
    column_config={
    "Chart": st.column_config.LineChartColumn("Chart", width="medium",
            help="The sales volume in the last 6 months",
            y_min=0,
            y_max=100,),
    
    }
)

ff
