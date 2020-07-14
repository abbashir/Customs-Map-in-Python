import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
name = list(data["NAME"])


def color_producer(elev_no):
    if elev_no < 1000:
        return "green"
    elif 1000 <= elev_no < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")
# for lt, ln, ele, name in zip(lat, lon, elev, name):
#     fg.add_child(
#         folium.Marker(location=[lt, ln], popup=str(ele), icon=folium.Icon(color=color_producer(ele))))

for lt, ln, ele, name in zip(lat, lon, elev, name):
    fg.add_child(
        folium.CircleMarker(location=[lt, ln], radius=10, fill_color=color_producer(ele), popup=str(ele),
                            color='gray', fill_opacity=0.7))

map.add_child(fg)
map.save("map.html")
