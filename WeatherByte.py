"""
WeatherByte - A simple weather dashboard built with Python and Tkinter.
It fetches real-time weather data from the OpenWeatherMap API.

Requirements:
- Python 3
- requests library
- tkinter (comes with standard Python)

How to Run:
- Make sure 'requests' is installed (`pip install requests`).
- Run this file using Python.

Author: Kamsy Onuora
Date: 26 April 2025
"""




import tkinter as tk # Imports the tkinter module for creating a GUI. 'tk' is an alias for easier usage.
import requests # Used to send HTTP requests to fetch data from the weather API.

#root is like the menu of the app
root = tk.Tk()#creates main window for tkinter app
root.configure(bg = "#87CEEB") #sets background to light blue colour 
root.title("WeatherByte - Your Weather Dashboard")#title of the window
root.geometry("400x300")#size of window
root.resizable(False, False)#width and length are not resizable

#loading 
loading_label = tk.Label(root, text="", font=("Helvetica", 12), bg="white", fg="gray")
loading_label.pack(pady=5)# adds vertical spacing 

def get_weather():
    city = city_entry.get()# gets the city name entered by user
    if not city.strip():  # If city entry is empty or only spaces
        weather_output.config(text="Please enter a city name.", fg="red")#shows error 
        return  # Stop the function, don't try to fetch weather
    loading_label.config(text="Loading... Please wait.", fg="gray")# Show loading animation 
    weather_output.config(text="")# Clear any old weather output
    
    weather = fetch_weather_data(city)  # Call the function to get weather
    loading_label.config(text="") #clear loading message once done

    # If there's an error, you show it
    if "error" in weather:
        weather_output.config(text=f"Error: {weather['error']}", fg = "red")#show error in red
    else:
        # Display weather info in the app
        weather_text = (
            f"City: {weather['city']}\n"
            f"🌡 Temperature: {weather['temperature']}°C\n"
            f"🌥 Description: {weather['description']}\n"
            f"💧 Humidity: {weather['humidity']}%"
            )
        weather_output.config(text=weather_text, fg="black") #updates the label with all weather info


#creates a label that asks user to enter a city
city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12), bg = "white", fg = "black") #go into tk toolbox and creates a label that lets you enter city
city_label.pack(pady=15)# pady(vertical spacing), pack means it goes at the top

#creates an entry that allows for typing
city_entry = tk.Entry(root, width=30, font=("Helvetica", 12))#creates textbox for typing
city_entry.pack(pady=5)
city_entry.pack()#pack means it goes below city label

#a button to look for the weather
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather,
    font=("Helvetica", 12), bg="white", fg="black", bd = 2, relief = "ridge") #creates a button
get_weather_button.pack(pady=15)#pack means it goes below city entry

#display the weather
weather_output = tk.Label(root, text="Weather info will appear here.",
    font=("Helvetica", 12, "bold"), bg="white", fg="black", width=40, height=8, bd=2, relief="groove", wraplength=300, justify="left") 
weather_output.pack(pady=20)#pack means it goes below get weather button




API_KEY = "your_new_api_key_here"  # your own API key from openweather
#function that actually fetches the data from the OpenWeather API key
def fetch_weather_data(city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric" #url to request data for the city in metric units 
        response = requests.get(url)#sends a GET request to the weather API
        data = response.json() # convert response to python dictionary

        if response.status_code == 200:
            # Extract the required weather information from the API response
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"].title(),
                "humidity": data["main"]["humidity"]
            }
            return weather #return weather data
        else:
            return {"error": data.get("message", "Error retrieving weather.")} #city not found, return this message
    except Exception as e:
        return {"error": str(e)} #problem with request, return error maybe like network
root.mainloop()# Start the GUI application loop
    

