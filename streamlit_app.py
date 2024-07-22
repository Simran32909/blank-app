import streamlit as st
import requests


def get_weather(city, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    return response.json()


def main():
    st.title("Basic Weather App ☁️  ")

    api_key = "59b6e63d1276b5840ae9f11d286dd7c3"
    city = st.text_input("Enter city name:")

    if city:
        weather_data = get_weather(city, api_key)

        if weather_data.get("cod") != "404":
            main_weather = weather_data["weather"][0]["main"]
            description = weather_data["weather"][0]["description"]
            temperature = weather_data["main"]["temp"]
            humidity = weather_data["main"]["humidity"]
            wind_speed = weather_data["wind"]["speed"]

            st.write(f"**Weather:** {main_weather}")
            st.write(f"**Description:** {description}")
            st.write(f"**Temperature:** {temperature}°C")
            st.write(f"**Humidity:** {humidity}%")
            st.write(f"**Wind Speed:** {wind_speed} m/s")
        else:
            st.write("City not found!")


if __name__ == "__main__":
    main()
