import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd

from PIL import Image

orgs = ["Dunzo", "Facebook", "Instagram",
        "Paypal", "Playstore", "Twitter", "Uber"]
csvs = {}

for i in orgs:
    org_csv = []
    for j in range(1, 5):
        csv = pd.read_csv("results/" + i.lower() + "/" + str(j) + "gram_tfidf.csv")
        org_csv.append(csv)

    csvs[i] = org_csv
