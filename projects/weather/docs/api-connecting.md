Next step is to use the location given to return the weather summary
I'll do this using the weather overview endpoint of the API

the API call looks like: 
https://openweather/data/3.0/onecall/overview?lat={lat}&lon={lon}&appid={API key}

so the parameters will look like:
params = {"lat":lat, "lon":lon, "appid":api_key}
requests.get("https://blahblah/overview", params=params)

there is:
- an optional units parameter which i might need to use to apply celsius
- an optional date parameter which can be used to get weather at a distant date

response from the API looks like:
{
   "lat": 51.509865,
   "lon": -0.118092,
   "tz": "+01:00",
   "date": "2024-05-13",
   "units": "metric",
   "weather_overview": "The current weather is overcast with a 
temperature of 16°C and a feels-like temperature of 16°C. 
The wind speed is 4 meter/sec with gusts up to 6 meter/sec 
coming from the west-southwest direction. 
The air pressure is at 1007 hPa with a humidity level of 79%. 
The dew point is at 12°C and the visibility is 10000 meters. 
The UV index is at 4, indicating moderate risk from the 
sun's UV rays. 
The sky is covered with overcast clouds, and there is 
no precipitation expected at the moment. 
Overall, it is a moderately cool and cloudy day 
with light to moderate winds from the west-southwest."
}

we just need data["weather_overview"] and maybe data["date"]

TO DO:
- [ ] still need to add the reading of the json file for lat and lon coords to the check for current location function

Found out that the API i was trying to use was not free so now I have to call the current weather data API
Then using that API I need to parse the information into reuseable vars so that I can return information according to user request

# Coords to Weather Information Function



