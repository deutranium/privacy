import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import pydeck as pdk

geodata = pd.read_csv("./assets/countries.csv")
EU = [
    "Austria",
    "Belgium",
    "Bulgaria",
    "Croatia",
    "Republic of Cyprus",
    "Czech Republic",
    "Denmark",
    "Estonia",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "Hungary",
    "Ireland",
    "Italy",
    "Latvia",
    "Lithuania",
    "Luxembourg",
    "Malta",
    "Netherlands",
    "Poland",
    "Portugal",
    "Romania",
    "Slovakia",
    "Slovenia",
    "Spain",
    "Sweden",
    "United Kingdom"
]

def gdpr_compliant_map():
    lt = [
        "Austria",
        "Belgium",
        "Bulgaria",
        "Croatia",
        "Republic of Cyprus",
        "Czech Republic",
        "Denmark",
        "Estonia",
        "Finland",
        "France",
        "Germany",
        "Greece",
        "Hungary",
        "Ireland",
        "Italy",
        "Latvia",
        "Lithuania",
        "Luxembourg",
        "Malta",
        "Netherlands",
        "Poland",
        "Portugal",
        "Romania",
        "Slovakia",
        "Slovenia",
        "Spain",
        "Sweden",
        "United Kingdom"
    ]

    gapminder = px.data.gapminder().query("year==2007")
    gapminder["GDPR Compliant"] = gapminder.apply(
        lambda row: True if row.country in lt else False, axis=1)
    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="GDPR Compliant",
                        hover_name="country",
                        color_discrete_map={0: "cyan", 1: "yellow"})
    st.plotly_chart(fig)


def fb_active_map():
    lt = ["China", "Iran", "Syria", "North Korea"]
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Facebook Active"] = gapminder.apply(
        lambda row: True if row.country not in lt else False, axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Facebook Active",
                        hover_name="country",
                        color_discrete_map={0: "cyan", 1: "yellow"})

    st.plotly_chart(fig)


def twitter_active_map():
    lt = ["China", "Iran", "North Korea"]

    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Twitter Active"] = gapminder.apply(
        lambda row: True if row.country not in lt else False, axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Twitter Active",
                        hover_name="country",
                        color_discrete_map={0: "cyan", 1: "yellow"})

    st.plotly_chart(fig)

def insta_active():
    lt = ["China", "Iran", "North Korea"]
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Instagram Active"] = gapminder.apply(lambda row: True if row.country not in lt else False , axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Instagram Active", 
                        hover_name="country", 
                        color_discrete_map={0:"cyan", 1:"yellow"})
    st.plotly_chart(fig)

def paypal_active():
    lt = {a:"EU" for a in EU}
    lt["United States"] = "US"
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Paypal Active"] = gapminder.apply(lambda row: "Others" if row.country not in lt else lt[row.country] , axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Paypal Active", 
                        hover_name="country", 
                        color_discrete_map={0:"cyan", 1:"yellow", 2:"green"})
    st.plotly_chart(fig)

def uber_active():
    lt = {a:"EU" for a in EU}
    lt["United States"] = "US"
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Uber Active"] = gapminder.apply(lambda row: "Others" if row.country not in lt else lt[row.country] , axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Uber Active", 
                        hover_name="country", 
                        color_discrete_map={0:"cyan", 1:"yellow", 2:"green"})
    st.plotly_chart(fig)

def uber_active_2():
    lt = {a:"EU" for a in EU}
    lt["United States"] = "US"

    ltdata = geodata.loc[geodata["name"].isin(lt)]
    # print(ltdata)

    # geodata["color"] = [240, 50, 120]
    selected_layers = pdk.Layer(
        "ScatterplotLayer",
        data=ltdata,
        get_position=["longitude", "latitude"],
        get_color=[200, 30, 0, 160],
        get_radius=2000,
        radius_scale=100,
    )
    # print(selected_layers)
    st.pydeck_chart(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={"latitude": 0,
                            "longitude": 0, "zoom": 1, "pitch": 20},
        layers=selected_layers,
    ))
