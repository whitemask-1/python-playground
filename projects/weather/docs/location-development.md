# Check For Current Location Function

- Currently we check if the config file exists:
    - if it does the read the location : *
    - otherwise create a new config file
        - ask for user input for a location
        - store the location in the config file

However I think it should run with latitude and longitude for the geocoder

## Geocoder Function

- It would have to pull from the geocoder api 
    - to convert the location input into latitude and longitude coords
    - however the input to the api must follow this structure:
        - If in the United States
            - use {CITY}, {STATE CODE}, {COUNTRY CODE}

        - Else
            - use {CITY}, {COUNTRY CODE}

So then what does use mean for me:
    
- Geocode function(user location) <- internal function
    - Best practice is to wrap the api call in try except
        - then raise the error to the current location function

    - to call the api we need to use the requests module 
    - http://api.openweathermap.org/geo/1.0/direct?q={city name},{state code},{country code}&limit={limit}&appid={API key}
    - the request.get looks like:
        - requests.get("https://etcetc/direct", params = params)
        - params = {"q":user_location, "limit":1, "appid":APIKEY}
    - obviously store api key in the env vars
    - the api response to the get request has a list of dicts of locations:
        - we will just take the first dict everytime and 
        - enforce the full params to get precise location
        - inside the dict are latitude and longitude vars:
            - denoted "lat" and "lon"

    - Grab the latitude and longitude 
    - return that to the check for current location function when writing



