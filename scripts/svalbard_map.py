import numpy as np
import pandas as pd
#import global_functions
import json
from bokeh.io import curdoc, output_file, show
from bokeh.layouts import column, row, WidgetBox
#from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure, output_file, show

from bokeh.models import (CategoricalColorMapper, HoverTool,
      ColumnDataSource, Panel, LinearColorMapper, Select,
      FuncTickFormatter, SingleIntervalTicker, LinearAxis,
      Paragraph, TextInput, GMapOptions, GeoJSONDataSource)

from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider,
      Tabs, CheckboxButtonGroup, Paragraph,
      TableColumn, DataTable, Select)

from bokeh.palettes import Viridis6, Spectral5
from bokeh.tile_providers import CARTODBPOSITRON, get_provider




def svalbard_map_tab(MTO):



    stations = ['ZEPPELIN','HORNSUND','PYRAMIDEN','KONGSØYA', 'KARL_XII-ØYA', 'KVITØYA' ,'SVEAGRUVA']
    coordinates = [[15.550000,77.000000],[11.8867,78.9072],[16.360300, 78.655700],[28.892000, 78.910800], [25.008000, 80.653000],
        [31.464300, 80.105800],[16.720000, 77.895300]]
    x = [item[0] for item in coordinates]
    y = [item[1] for item in coordinates]
    #x = [19.10797119140625, 15.550000, 11.8867]#, -96.79, -97.33, -95.36, -98.49]
    #y = [74.51878916336756, 77.000000, 78.9072]#, 32.77, 32.75, 29.76, 29.42]
    # Set up widgets
    #station = 'ZEPPELIN'
    map_para = Paragraph(text= '', width=100, height=100)
    station_select = Select(value=stations[0], title='Stations', options=stations)


    # Set up callbacks
    def update_text(attrname, old, new):
        station = station_select.value
        map_para.text = station

    station_select.on_change('value', update_text)



    # Set up layouts and add to document
    # JSON
    # reading the data from the file

    # Set up svalbard Map
    with open('svalbard.json') as f:
        svalbard = f.read()
        data = json.loads(svalbard)
        geo_source = GeoJSONDataSource(geojson=svalbard)

    mapSvalbard = figure(title='Svalbard', x_axis_location=None,
                            y_axis_location=None, plot_height=400,
                            plot_width=400)
    mapSvalbard.outline_line_color = None
    mapSvalbard.xgrid.grid_line_color = None
    mapSvalbard.ygrid.grid_line_color = None

    color_mapper = LinearColorMapper(palette=Viridis6)
    mapSvalbard.patches('xs', 'ys', source=geo_source)#, fill_alpha=0.7, fill_color={'field': 'objectid', 'transform': color_mapper},


    # Adding Stations to map

    # The scatter markers
    mapSvalbard.circle(x, y, size=8, color='red', alpha=1)
    mapSvalbard.select(name="mycircle")
    hover = mapSvalbard.select_one(HoverTool)
    #hover.point_policy = "follow_mouse"
    #hover.tooltips = [("Provincia:", "@provincia")]
    show(mapSvalbard)

    #folium.Marker(location=[ 77.000000, 15.550000 ], popup='Hornsund Station</b>',

    #folium.Marker(location=[78.9072, 11.8867],popup='Zeppelin Station</b>',


    inputs = row(station_select, map_para)
    layout = column(mapSvalbard,inputs, width=1000)
    tab = Panel(child = layout, title = 'Svalbard Map')

    return tab
