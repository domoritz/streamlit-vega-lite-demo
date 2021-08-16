import streamlit as st
import pandas as pd
import altair as alt
from streamlit_vega_lite import altair_component

st.title("Penguin Data Explorer 🐧")

st.write("Hover over the scatterplot to reveal details about a penguin. The code for this demo is at https://github.com/domoritz/streamlit-vega-lite-demo.")

@st.cache
def load(url):
    return  pd.read_json(url)

df = load("https://cdn.jsdelivr.net/npm/vega-datasets@2/data/penguins.json")

if st.checkbox("Show Raw Data"):
    st.write(df)

@st.cache
def make_altair_scatterplot():
    selected = alt.selection_single(on="mouseover", empty="none")

    return alt.Chart(df).mark_circle(size=150).encode(
        alt.X("Body Mass (g)", scale=alt.Scale(zero=False)),
        alt.Y("Flipper Length (mm)", scale=alt.Scale(zero=False)),
        color=alt.condition(selected, alt.value("red"), alt.value("steelblue"))
    ).add_selection(selected)


selection = altair_component(make_altair_scatterplot())

if "_vgsid_" in selection:
    # the ids start at 1
    st.write(df.iloc[[selection["_vgsid_"][0] - 1]])
else:
    st.info("Hover over the chart above to see details about the Penguin here.")
