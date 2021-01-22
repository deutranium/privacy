import streamlit as st
import plotly.express as px
import numpy as np

from components.maps import *
from components.wordclouds import *
from components.ngrams import *


companies = ("Dunzo", "Facebook", "Instagram", "Paypal", "Playstore", "Twitter", "Uber")

st.title("Privacy Visualisations")
st.markdown("Lorem ipsum dolor sit amet")

# MAPS start
st.header("Maps")

gdpr_compliant_map()
st.markdown("Lorem ipsum dolor sit amet")
st.markdown("----")

fb_active_map()
st.markdown("Lorem ipsum dolor sit amet")
st.markdown("----")

twitter_active_map()
st.markdown("Lorem ipsum dolor sit amet")
st.markdown("----")

insta_active()
st.markdown("Lorem ipsum dolor sit amet")
st.markdown("----")

# MAPS end


# WORDCLOUDS start

st.header("Wordclouds")

val = st.selectbox(
    'Company name: ',
    companies
)

gram = st.selectbox(
    'Gram: ',
    (1, 2, 3, 4)
)

st.image(images[val][gram-1], use_column_width=True)

# WORDCLOUDS end


# TFIDF start

st.header("Wordclouds")

org = st.selectbox(
    'Company name:',
    companies
)

csv = st.selectbox(
    'Gram:',
    (1, 2, 3, 4)
)

st.write(csvs[org][csv-1], use_column_width=True)

# TFIDF end
