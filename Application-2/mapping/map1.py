import folium
import pandas as pd

data = pd.read_csv("original.txt")

lat = list(data['LAT'])
long = list(data['LON'])
elevation = list(data['ELEV'])

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")

for i , j, k in zip(lat, long, elevation):
    fgv.add_child(folium.CircleMarker(location=[i, j], radius=6, popup=str(k),
                                     fill_color= "green" if 0<=k and k<1000 else ("purple" if 1000<=k and k<2000 else "orange"),
                                     color = "grey", fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(),
                            style_function = lambda  x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
                                                        else 'orange' if 10000000 <= x['properties']['POP2005'] < 25000000
                                                         else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map1.html")
