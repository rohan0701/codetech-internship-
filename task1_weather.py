"""
CODTECH Internship - Task 1
API Integration & Data Visualization
Author: Rohan
"""

import requests
import matplotlib.pyplot as plt

# ----------------------------
# 1. API Configuration
# ----------------------------
API_KEY = "https://samples.openweathermap.org/data/2.5/weather?q=London&appid=b6907d289e10d714a6e88b30761fae22"   # Replace with your OpenWeatherMap API Key
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ----------------------------
# 2. Fetch Weather Data
# ----------------------------
response = requests.get(URL)
data = response.json()

if response.status_code != 200:
    print("Error fetching data:", data)
    exit()

# ----------------------------
# 3. Extract Dates & Temperatures
# ----------------------------
dates = [item['dt_txt'] for item in data['list'][:10]]   # First 10 entries
temps = [item['main']['temp'] for item in data['list'][:10]]

# ----------------------------
# 4. Visualization
# ----------------------------
plt.figure(figsize=(10, 5))
plt.plot(dates, temps, marker='o', color='blue', linestyle='--')
plt.title(f"Weather Forecast for {CITY}", fontsize=14)
plt.xlabel("Date/Time", fontsize=12)
plt.ylabel("Temperature (°C)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save plot
plt.savefig("weather_plot.png")
plt.show()

print("Weather plot saved as weather_plot.png")
