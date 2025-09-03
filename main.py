import streamlit as st
import plotly.express as px
from backend import getdata
st.title("Weather Forecast for the Next Days")
place=st.text_input("Place: ")
slider=st.slider("Forecast Days",min_value=1,max_value=5,help="Select the number of forecasted days")
option=st.selectbox("Select data to view",("Temperature",
                                           "Sky"))
st.subheader(f"{option} for the next {slider} in {place}")
try:
    if place:
        filtered_data=getdata(place,slider)
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (°C)"})
            figure.update_yaxes(tickformat=".2f")  # Show decimals
            st.plotly_chart(figure)
        if option=="Sky":
            sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
            dates = [item["dt_txt"] for item in filtered_data]

            sky_images = {
                "Clear": "https://cdn-icons-png.flaticon.com/512/869/869869.png",
                "Clouds": "https://cdn-icons-png.flaticon.com/512/414/414825.png",
                "Rain": "https://cdn-icons-png.flaticon.com/512/116/116251.png",
                "Snow": "https://cdn-icons-png.flaticon.com/512/642/642102.png"
            }
            image_urls = [sky_images.get(condition, sky_images["Clouds"]) for condition in sky_conditions]
            st.image(image_urls, caption=dates, width=80)
except KeyError:
    st.write("That place doesnt exist")





