from geopy.geocoders import Nominatim

def get_coordinates(city_name):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city_name)
    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None

city_name = input("请输入城市名: ")
coordinates = get_coordinates(city_name)

if coordinates:
    print(f"城市 {city_name} 的经纬度为: {coordinates[0]}, {coordinates[1]}")
else:
    print("无法获取该城市的经纬度信息")
