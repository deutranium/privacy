import streamlit as st
import plotly.express as px
import numpy as np

from PIL import Image

orgs = ["Dunzo", "Facebook", "Instagram",
        "Paypal", "Playstore", "Twitter", "Uber"]
images = {}

for i in orgs:
    org_imgs = []
    for j in range(1, 5):
        img = Image.open("wordclouds/" + i.lower() + "/wordcloud gram" + str(j) + ".png")
        org_imgs.append(img)

    images[i] = org_imgs
