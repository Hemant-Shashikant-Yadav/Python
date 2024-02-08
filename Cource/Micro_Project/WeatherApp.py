# importing modules
import requests
import json

# setting up API
api_key = "e67c1f157951a09e4c1d6269d7028c50"

print("Enter the location as exit if you want to exit the program")


def ApiFunc():
    location = input("Enter the city location : ")
    # exiting if the location is entered as exit
    if location == "exit":
        print("The program has been terminated successfully...")
        exit()
    try:
        api_str = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
        # converting recieved api response from string to dictionary
        req_str = requests.get(api_str)
        req_dict = json.loads(req_str.text)

        # getting data from API
        temp_celc = "%.2f" % (req_dict["main"]["temp"] - 273.15)
        max_temp_celc = "%.2f" % (req_dict["main"]["temp_max"] - 273.15)
        min_temp_celc = "%.2f" % (req_dict["main"]["temp_min"] - 273.15)
        humidity = req_dict["main"]["humidity"]
        pressure = req_dict["main"]["pressure"]
        weather = req_dict["weather"][0]["description"]
        longitute = req_dict["coord"]["lon"]
        latitude = req_dict["coord"]["lat"]

        # printing out the data
        print(f"city: {location}\tlongitude: {longitute}\tlatitude: {latitude}")
        print(
            f"min temperature: {min_temp_celc}\tmax temperature: {max_temp_celc}\taverage temerature: {temp_celc}"
        )
        print(f"humidity: {humidity}\tpressure: {pressure}\tweather: {weather}")

    except:
        print("Location not found please re-enter the location")
    # recursion in both cases even if the program goes into the `try` block or `expect` block until the
    # `location`!="exit"
    ApiFunc()


ApiFunc()
