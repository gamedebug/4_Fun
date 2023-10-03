from math import radians, cos, sin, asin, sqrt
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

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # 将经纬度转换为弧度
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine公式
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # 地球半径，单位为千米
    return c * r

city1_name = input("请输入第一个城市名: ")
coordinates_1 = get_coordinates(city1_name)
city2_name = input("请输入第二个城市名: ")
coordinates_2 = get_coordinates(city2_name)
print(haversine(coordinates_1[0], coordinates_1[1], coordinates_2[0], coordinates_2[1]))
