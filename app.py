import streamlit as st
import plotly.express as px
import numpy as np

from components.maps import *
from components.wordclouds import *
from components.ngrams import *
from components.readability import *

# Similarity file commented out because as it downloads a 1.6gb model everytime ir runs
# from components.similarity import *

companies = ("Dunzo", "Facebook", "Instagram",
             "Paypal", "Playstore", "Twitter", "Uber")

# Call functions ased on map value
mapFunc = {
    "GDPR Compliant Countries": gdpr_compliant_map,
    "Facebook": fb_active_map,
    "Twitter": twitter_active_map,
    "Instagram": insta_active,
    "Paypal": paypal_active,
    "Uber": uber_active
}

# BODY STARTS HERE

st.title("Privacy Visualisations")

# MAPS start
st.header("Maps")

mapOpt = st.selectbox(
    'Select option: ',
    ("GDPR Compliant Countries", "Facebook", "Twitter", "Instagram", "Paypal", "Uber")
)

if mapOpt != "GDPR Compliant Countries":
    st.write("Privacy policy is consistent in like colored regions")
mapFunc[mapOpt]()
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

# Data stored as CSV to make the app faster

# convert to CSV
# df = ReadabilityScores()
# csv = df.to_csv('./assets/readability.csv')
# st.write(df)

csv_readability = pd.read_csv('./assets/readability.csv')
csv_readability.set_index('Company', inplace=True)
st.dataframe(csv_readability.style.format("{:.2f}"))

# READIBILITY SCORES END

# SMILARITY SCORES END
st.header("Similarity Scores")
csv_similarity = pd.read_csv('./assets/similarity.csv')
df_similarity = pd.DataFrame(csv_similarity)

df_similarity = df_similarity.set_index('Company')

st.table(df_similarity)
# SIMILARITY SCORES END
