import tkinter as tk
import requests
import json
from datetime import datetime

# Create the window
window = tk.Tk()
window.title("Smart Mirror")
window.geometry("800x480")

# Display the time on the mirror
time_label = tk.Label(window, font=("Helvetica", 45), fg="white", bg="black")
time_label.pack(side="top", fill="both", expand=True)

# Display the weather information on the mirror
weather_label = tk.Label(window, font=("Helvetica", 20), fg="white", bg="black")
weather_label.pack(side="top", fill="both", expand=True)

# Update the time and date
def update_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    window.after(1000, update_time)

# Update the weather information
def update_weather():
    city = "Coimbatore"
    url="http://api.weatherstack.com/current?access_key=654eb527e5e6985e598915bff703ef62&query="+city
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)
    weather = data["current"]["weather_descriptions"][0]
    temp = data["current"]["temperature"]
    weather_label.config(text="Weather:{}\n Temperature:{} °C\n".format(weather,temp))
    window.after(60000, update_weather)

# Continuously update the display
update_time()
update_weather()

# Run the window
window.mainloop()

