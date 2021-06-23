from datetime import datetime
from django.shortcuts import render
import folium
from .models import Doc
from django.db.models import Count

def index(request):
    return render(request, 'index.html')

def map(request,date):

    #Create Map
    m = folium.Map(location=[20,0], zoom_start=1)

    docs=Doc.objects.filter(date=datetime.strptime(date, '%Y%m%d'))
    countries = Doc.objects.filter(date=datetime.strptime(date, '%Y%m%d')).values('country').annotate(nums=Count('country')).order_by('nums').reverse()

    #Add Markers
    for i in docs:
        folium.CircleMarker(location=(i.latitude, i.longitude),
                            radius=5, fill_color='blue',
                            popup='Country:' + i.country + '\nCity:' + i.city).add_to(m)
    #Add TileLayer
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)

    #Get HTML representation of map
    m = m._repr_html_()
    context = {
        'node_count':docs.count(),
        'countries':countries,
        'date':date,
        'm': m
    }
    return render(request, 'map.html', context)