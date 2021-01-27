import streamlit as st
import plotly.express as px
import numpy as np

from components.maps import *
from components.wordclouds import *
from components.ngrams import *
from components.readability import *
# from components.similarity import *

companies = ("Dunzo", "Facebook", "Instagram", "Paypal", "Playstore", "Twitter", "Uber")

st.title("Privacy Visualisations")

# MAPS start
st.header("Maps")

gdpr_compliant_map()
st.markdown("### GDPR Compliant Countries")
st.markdown("----")

fb_active_map()
st.markdown("### Facebook privacy policy across the map")
st.markdown("Privacy policy is consistent in like colored regions")
st.markdown("----")

twitter_active_map()
st.markdown("### Twitter privacy policy across the map")
st.markdown("Privacy policy is consistent in like colored regions")
st.markdown("----")

insta_active()
st.markdown("### Instagram privacy policy across the map")
st.markdown("Privacy policy is consistent in like colored regions")
st.markdown("----")

paypal_active()
st.markdown("### Paypal privacy policy across the map")
st.markdown("Privacy policy is consistent in like colored regions")
st.markdown("----")

uber_active()
st.markdown("### Uber privacy policy across the map")
st.markdown("Privacy policy is consistent in like colored regions")
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

st.header("N-Grams")

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

# READIBILITY SCORES
st.header("Readability Scores")

st.write(ReadabilityScores())

# READIBILITY SCORES END
