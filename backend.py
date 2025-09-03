import requests

API_KEY="1d05b2723e25e105f8beb931a5f80e66"
def getdata(place,forecast_days,):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data = response.json()
    filtered_data=data["list"]
    no = 8 * forecast_days
    filtered_data = filtered_data[:no]
    return filtered_data





if __name__=="__main__":
    print(getdata(place="tokyo",forecast_days=3))
