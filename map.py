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
fgv = folium.FeatureGroup(name="Volcanoes")
# for lt, ln, ele, name in zip(lat, lon, elev, name):
#     fg.add_child(
#         folium.Marker(location=[lt, ln], popup=str(ele), icon=folium.Icon(color=color_producer(ele))))


for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=str(el) + " m",
                                      fill_color=color_producer(el), fill=True, color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                             else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map.html")
