import requests


api_key = "0aa441ed77913b236cf94cf2b2f2a242"

def get_data(place = "Dhaka", forecast_days = None):    
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    values = 8 * forecast_days

    filtered_data = filtered_data[:values]

    return filtered_data

if __name__ == "__main__":
    print(get_data(place="Dhaka"))