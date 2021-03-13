import numpy as np
import pandas as pd
import os
from bokeh.io import curdoc
from bokeh.layouts import column, row, WidgetBox
#from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

from bokeh.models import (CategoricalColorMapper, HoverTool,
      ColumnDataSource, Panel, MultiSelect,
      FuncTickFormatter, SingleIntervalTicker, LinearAxis,DateRangeSlider,
                          TextInput)

from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider,
      Tabs, CheckboxButtonGroup,
      TableColumn, DataTable, Select)

from bokeh.palettes import Category20_16, Spectral5


STATIONS = ['Zeppelin','Hornsund']
def weather_tab(MTO_data):

    # Read Files in data directory
    filesData = []
    tmp = 1
    path = r"C:/Users/MATEO/Documents/infoTeo/Personal_Projects/Hack_the_Artic/svalboard/data/"
    for files in os.listdir(path):
        if os.path.isfile(os.path.join(path, files)):
            filesData.append((str(tmp),files))
            tmp = tmp + 1
    # Read datapa
    #df = pd.read_csv(r'../data/carbon_data.csv')
    df = pd.read_csv(r'C:\Users\MATEO\Documents\infoTeo\Personal_Projects\Hack_the_Artic\svalboard\data\carbon_data.csv')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+'WORKED'+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
    yLabels = df.columns.values
    yLabels = list(yLabels[1:])

    #discrete = [x for x in columns if df[x].dtype == object]
    #continuous = [x for x in columns if x not in discrete]


    def make_plot():
        y_title = yAxis.value.title()
        print(y_title+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
        #xs = list(df['Unnamed: 0'].values.index)
        xs = list(pd.to_datetime(df['Unnamed: 0']).values)
        ys = list(df[y_title].values)

        init_date = pd.to_datetime(df['Unnamed: 0']).values.min()
        final_date = pd.to_datetime(df['Unnamed: 0']).values.max()
        #print(xs)
        curdoc().theme = 'dark_minimal'


        plot = figure(x_axis_type='datetime',plot_height=400, plot_width=800, title=y_title,
                      tools="crosshair,pan,reset,save,wheel_zoom,hover,box_zoom",
                      x_range=[date_range_slider.value[0], date_range_slider.value[1]])

        plot.circle(x=xs, y=ys, line_color="white", alpha=0.6, hover_color='white', hover_alpha=0.5)

        # fixed attributes
        #plot.xaxis.formatter = bokeh.models.formatters.DatetimeTickFormatter(months=["%m-%d-%Y"])
        plot.xaxis.axis_label = "Date"
        plot.yaxis.axis_label = unitsLabel.value
        plot.axis.axis_label_text_font_style = "bold"
        plot.grid.grid_line_alpha = 0.3

        return plot
        # Set up callbacks
    def update(attr, old, new):
    	layout.children[1] = make_plot()

    #def update_units_y(attrname, old, new):
        #plot.yaxis.axis_label = unitsLabel.value
        #layout.children[1] = make_plot()

    # Set up widgets
    unitsLabel = TextInput(title="Units", value='None')
    unitsLabel.on_change('value', update)

    yAxis = Select(title='Y-Axis', value=yLabels[0], options=yLabels)
    yAxis.on_change('value', update)

    dataSelect = MultiSelect(title='Datasets', value=["1"], options=filesData)
    dataSelect.on_change('value', update)


    init_date = pd.to_datetime(df['Unnamed: 0']).values.min()
    final_date = pd.to_datetime(df['Unnamed: 0']).values.max()
    date_range_slider = DateRangeSlider(value=(init_date, final_date),
                                    start=init_date, end=final_date)
    date_range_slider.on_change("value", update)

    plot = make_plot()

    # set up layout
    inputs = column(dataSelect, yAxis, unitsLabel,date_range_slider)
    layout = row(inputs, plot, width=2000)

    #layout = row(inputs, plot, width=800)
    tab = Panel(child = layout, title = 'Weather')
    return tab
