import requests
import wx
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

def get_weather(city_name):
    if get_coordinates(city_name):
        lat = get_coordinates(city_name)[0]
        lon = get_coordinates(city_name)[1]
        url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid=b17e74bdfca8d42687a95bc26e0f5f1b"
        response = requests.get(url)
        data = response.json()

        # 获取当前天气信息
        current_weather = data["current"]["weather"][0]["description"]
        temperature = data["current"]["temp"]
        temperature = round(temperature - 273.15, 2)
        return current_weather, temperature
    else:
        return None

class WeatherFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="天气查询")

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        location_label = wx.StaticText(panel, label="城市:")
        self.location_entry = wx.TextCtrl(panel)
        vbox.Add(location_label, flag=wx.ALL, border=10)
        vbox.Add(self.location_entry, flag=wx.EXPAND|wx.ALL, border=10)
        
        #lat_label = wx.StaticText(panel, label="纬度:")
        #self.lat_entry = wx.TextCtrl(panel)
        #vbox.Add(lat_label, flag=wx.ALL, border=10)
        #vbox.Add(self.lat_entry, flag=wx.EXPAND|wx.ALL, border=10)

        #lon_label = wx.StaticText(panel, label="经度:")
        #self.lon_entry = wx.TextCtrl(panel)
        #vbox.Add(lon_label, flag=wx.ALL, border=10)
        #vbox.Add(self.lon_entry, flag=wx.EXPAND|wx.ALL, border=10)

        submit_button = wx.Button(panel, label="显示天气")
        submit_button.Bind(wx.EVT_BUTTON, self.on_submit)
        vbox.Add(submit_button, flag=wx.ALL|wx.CENTER, border=10)

        self.result_label = wx.StaticText(panel, label="", style=wx.ALIGN_CENTER)
        vbox.Add(self.result_label, flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, border=10)

        panel.SetSizer(vbox)

    def on_submit(self, event):
        # 从输入框中获取城市名称
        location = self.location_entry.GetValue()
        # 从输入框中获取纬度和经度
        # lat = self.lat_entry.GetValue()
        # lon = self.lon_entry.GetValue()

        # 调用获取天气信息的函数
        #weather_info = get_weather(lat, lon)
        weather_info = get_weather(location)

        # 在界面上显示天气信息
        self.result_label.SetLabel(f"Current weather: {weather_info[0]}, Temperature: {weather_info[1]}°C")
        self.result_label.Wrap(self.GetSize()[0])  # 自动换行以适应窗口宽度
        self.result_label.SetWindowStyle(wx.ALIGN_CENTER_HORIZONTAL)  # 设置文本水平居中


if __name__ == "__main__":
    app = wx.App()
    frame = WeatherFrame()
    frame.Show()
    app.MainLoop()
