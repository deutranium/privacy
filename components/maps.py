import streamlit as st
import plotly.express as px
import numpy as np

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
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa"})
    st.plotly_chart(fig)


def fb_active_map():
    lt = ["China", "Iran", "Syria", "North Korea"]
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Facebook Active"] = gapminder.apply(
        lambda row: True if row.country not in lt else False, axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Facebook Active",
                        hover_name="country",
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa"})

    st.plotly_chart(fig)


def twitter_active_map():
    lt = ["China", "Iran", "North Korea"]

    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Twitter Active"] = gapminder.apply(
        lambda row: True if row.country not in lt else False, axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Twitter Active",
                        hover_name="country",
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa"})

    st.plotly_chart(fig)


def insta_active():
    lt = ["China", "Iran", "North Korea"]
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Instagram Active"] = gapminder.apply(
        lambda row: True if row.country not in lt else False, axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Instagram Active",
                        hover_name="country",
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa"})
    st.plotly_chart(fig)


def paypal_active():
    lt = {a: 0 for a in EU}
    lt["United States"] = 2
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Paypal Active"] = gapminder.apply(
        lambda row: 1 if row.country not in lt else lt[row.country], axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Paypal Active",
                        hover_name="country",
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa", 2: "#00b3fa"})
    st.plotly_chart(fig)


def uber_active():
    lt = {a: 0 for a in EU}
    lt["United States"] = 2
    gapminder = px.data.gapminder().query("year==2007")
    gapminder["Uber Active"] = gapminder.apply(
        lambda row: 1 if row.country not in lt else lt[row.country], axis=1)

    fig = px.choropleth(gapminder, locations="iso_alpha",
                        color="Uber Active",
                        hover_name="country",
                        color_discrete_map={0: "#ff8c69", 1: "#00b3fa", 2: "#00b3fa"})
    st.plotly_chart(fig)
