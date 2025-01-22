import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast App")
Place = st.text_input("Enter the place for weather forecast")

Days = st.slider("Days", min_value=1, max_value=7, help="Select the number of days for weather forecast")

option = st.selectbox("Select the type of weather forecast", ["Temperature", "Weather", "Wind Speed"])
st.subheader(option + " in " + Place + " for the next " + str(Days) + " days")

if Place:
    try:
        date, data = get_data(Place, Days, option)
        if option == "Temperature":
            choice = "Temperature in °C"
        elif option == "Weather":
            choice = "Weather"
        elif option == "Wind Speed":
            choice = "Wind Speed in m/s"
        figure = px.line(x=date, y=data, labels={"x": "Date", "y": choice})
        st.plotly_chart(figure)
    except KeyError:
        st.error("Please enter a valid place")