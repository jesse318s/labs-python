import folium
import webbrowser

map1 = folium.Map(location=[32.450, -99.714], zoom_start =12)
folium.CircleMarker(location=[32.450, -99.714], 
                    radius = 650, popup="Abilene").add_to(map1)
folium.Marker([32.613, -99.815]).add_to(map1)
folium.Marker([32.450, -99.714]).add_to(map1)
folium.Marker([30.275, -97.740]).add_to(map1)
folium.Marker([31.637, -97.084]).add_to(map1)

folium.PolyLine(locations = [(32.450, -99.714), (32.613, -99.815), (30.275, -97.740), (31.637, -97.084)],
                line_opacity = .6).add_to(map1)
map1.save("JSitesMap.html")
#open in browser
webbrowser.open("JSitesMap.html")
