import requests
from bs4 import BeautifulSoup


def get_current_temperature(station_id):
    temperature = 15

    return temperature
    

def calculate_pressure_altitude(elevation, altimeter_setting):
    standard_pressure = 29.92  # Standard pressure at sea level in inches of Mercury (inHg)
    pressure_altitude = (standard_pressure - altimeter_setting) * 1000 + elevation
    return pressure_altitude


def calculate_takeoff_performance(base_distance, base_ground_roll, weight, std_weight, pressure_altitude, current_temp, wind_component):
    weight_factor = weight / std_weight
    altitude_factor = 1 + 0.03 * (pressure_altitude / 1000)
    temperature_deviation = current_temp - 15
    temperature_factor = 1 + 0.01 * (temperature_deviation / 10)

    if wind_component > 0:
        wind_factor = 1 - (wind_component / 20)
    else:
        wind_factor = 1 + (abs(wind_component) / 20)

    takeoff_distance = base_distance * weight_factor * altitude_factor * temperature_factor * wind_factor
    takeoff_ground_roll = base_ground_roll * weight_factor * altitude_factor * temperature_factor * wind_factor

    return takeoff_distance, takeoff_ground_roll


def main():
    base_distance = 1800
    base_ground_roll = 910
    base_short_field_distance = 1500
    base_short_field_ground_roll = 900
    short_field_factor = 1

    weight = float(input("Enter aircraft weight (lbs): "))
    wind_component = float(input("Enter headwind component (knots): "))
    std_weight = 2550
    station_id = "KGFK"
    field_elevation = 0

    current_temp = get_current_temperature(station_id)
    print(f"Current Temperature: {current_temp}°C")
    altimeter_setting = 29.92
    pressure_altitude = calculate_pressure_altitude(field_elevation, altimeter_setting)
    print(f"Pressure Altitude: {pressure_altitude:.2f} feet")

    takeoff_distance, takeoff_ground_roll = calculate_takeoff_performance(base_distance, base_ground_roll, weight, std_weight, pressure_altitude, current_temp, wind_component)
    short_field_takeoff_distance, short_field_takeoff_ground_roll = calculate_takeoff_performance(base_short_field_distance, base_short_field_ground_roll, weight, std_weight, pressure_altitude, current_temp, wind_component)

    short_field_takeoff_distance *= short_field_factor
    short_field_takeoff_ground_roll *= short_field_factor

    print("\nNormal Takeoff:")
    print(f"  - Takeoff Distance: {takeoff_distance:.2f} feet")
    print(f"  - Takeoff Ground Roll: {takeoff_ground_roll:.2f} feet")
    print("\nShort Field Takeoff:")
    print(f"  - Takeoff Distance: {short_field_takeoff_distance:.2f} feet")
    print(f"  - Takeoff Ground Roll: {short_field_takeoff_ground_roll:.2f} feet")

main()