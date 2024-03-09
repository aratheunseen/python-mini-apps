import streamlit as st
import plotly.express as px
from controllers import get_data

st.title("Weather Forecast Dashboard")

place = st.text_input("Place")
days = st.slider("Forecast Days",min_value=1,max_value=5,
                 help="Select number for forecast days.")
view = st.selectbox("Select data to view",("Temperatue","Sky condition"))

if place:
    st.subheader(f"{view} for the next {days} days in {place}")

    try:
        filtered_data = get_data(place=place, forecast_days=days)
        

        if view == "Temperatue":
            dates = [dict["dt_txt"] for dict in filtered_data]
            temperatures = [dict["main"]["temp"]/10 for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperature (C)"})
            st.plotly_chart(figure)

        if view == "Sky condition":
            dates = [dict["dt_txt"] for dict in filtered_data]
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            imagepaths = [(f'images/{status.lower()}.png') for status in sky_conditions]

            st.image(imagepaths,width=130)

    except KeyError:
        error = f"{place} is not a valid place."
        st.error(error)