import requests
API_KEY = "e16339614c05554f4b2292b09418899c"
def get_data(place, days, option):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    value = response.json()
    filtered_data = value["list"]
    nr_values = 8 * days
    filtered_data = filtered_data[:nr_values]  # Get the first 8 values
    if option == "Temperature":
        temp = [value["main"]["temp"] / 10 for value in filtered_data]
        date = [value["dt_txt"] for value in filtered_data]
    elif option == "Weather":
        temp = [value["weather"][0]["main"] for value in filtered_data]
        date = [value["dt_txt"] for value in filtered_data]
    elif option == "Wind Speed":
        temp = [value["wind"]["speed"] for value in filtered_data]
        date = [value["dt_txt"] for value in filtered_data]
    return date, temp
