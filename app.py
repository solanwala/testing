import streamlit as st

ff = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

ff = st.data_editor(
    ff,
    column_config={
    "Chart": st.column_config.LineChartColumn(ff)
    }
)

ff
