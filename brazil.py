import folium

brazil = folium.Map(

  location = [-16.1237611, -59.9219642],
  zoom_start=4

)

folium.Marker(

  location = [-7.0849435, -34.8348102],
  popup = 'This script was coded here'
  
).add_to(brazil)


brazil.save('brazil.html')
