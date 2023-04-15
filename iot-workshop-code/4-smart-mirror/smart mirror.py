import tkinter as tk
import requests
import json
from datetime import datetime

# Create the window
window = tk.Tk()
window.title("Smart Mirror")
window.geometry("800x480")

# Display the time on the mirror
time_label = tk.Label(window, font=("Helvetica", 60), fg="white", bg="black")
time_label.pack(side="top", fill="both", expand=True)

# Display the weather information on the mirror
weather_label = tk.Label(window, font=("Helvetica", 30), fg="white", bg="black")
weather_label.pack(side="top", fill="both", expand=True)

# Update the time and date
def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Update the weather information
def update_weather():
    api_key = "your_api_key_here"
    city = "New York"
    url = "http://api.openweathermap.org/data/2.5/weather?q=coimbatore&units=imperial&appid=8fbbe029dddc03ee1eb8727906bb9199"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    weather_label.config(text="{weather}, {temp} °F")
    window.after(60000, update_weather)

# Continuously update the display
update_time()
update_weather()

# Run the window
window.mainloop()
