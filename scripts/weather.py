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



HoverTool(
    tooltips=[
        ( 'x',   '@x{%F}'            ),
        ( 'y',  '$@{y}{%0.2f}' ), # use @{ } for field names with spaces
    ],

    formatters={
        '@x'        : 'datetime', # use 'datetime' formatter for '@date' field
        '@y' : 'printf',   # use 'printf' formatter for '@{adj close}' field
                                     # use default 'numeral' formatter for other fields
    })
def weather_tab(MTO_data):

    # Read Files in data directory
    filesData = []
    tmp = 1
    path = r"C:/Users/MATEO/Documents/infoTeo/Personal_Projects/Hack_the_Artic/svalboard/data/"
    for files in os.listdir(path):
        if os.path.isfile(os.path.join(path, files)):
            #filesData.append((str(tmp),files))
            filesData.append(files)
            tmp = tmp + 1
    # Read datapa
    #df = pd.read_csv(r'../data/carbon_data.csv')
    #df = pd.read_csv(r'C:\Users\MATEO\Documents\infoTeo\Personal_Projects\Hack_the_Artic\svalboard\data\carbon_data.csv')
    #print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+'WORKED'+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
    #yLabels = df.columns.values
    #yLabels = list(yLabels[1:])

    #discrete = [x for x in columns if df[x].dtype == object]
    #continuous = [x for x in columns if x not in discrete]

    def make_plot():
        y_title1 = yAxis.value.title()
        y_title2 = yAxis2.value.title()
        #print(y_title+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
        #xs = list(df['Unnamed: 0'].values.index)
        #xs = list(pd.to_datetime(df['Unnamed: 0']).values)
        print(df1.columns)
        ys1 = list(df1[y_title1].values)
        ys2 = list(df2[y_title2].values)
        xs = xData

        #init_date = pd.to_datetime(df['Unnamed: 0']).values.min()
        #final_date = pd.to_datetime(df['Unnamed: 0']).values.max()
        #print(xs)

        #source = ColumnDataSource(data=dict(
        #    x = xs,
        #    y = ys,
        #    plot = yAxis.value.title(),
        #))


        #title=y_title,
        plot = figure(x_axis_type='datetime',plot_height=400, plot_width=800,
                      tools="crosshair,pan,reset,save,wheel_zoom,hover,box_zoom",
                      x_range=[date_range_slider.value[0], date_range_slider.value[1]])#,
                      #tooltips=HoverTool.tooltips)

        plot.circle(xs, ys1, line_color="white", alpha=0.6,
                        hover_color='white', hover_alpha=0.5)

        plot.circle(xs, ys2, line_color="red", alpha=0.6,
                        hover_color='red', hover_alpha=0.5)

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



    dataSelect = Select(title='Datasets 1', value=filesData[0], options=filesData)
    dataSelect.on_change('value', update)

    dataSelect2 = Select(title='Datasets 2', value=filesData[0], options=filesData)
    dataSelect2.on_change('value', update)

    # Read datapa
    #df = pd.read_csv(r'../data/carbon_data.csv')
    #dir_path = os.path.dirname(os.path.realpath(__file__))
    path = r'C:/Users/MATEO/Documents/infoTeo/Personal_Projects/Hack_the_Artic/stable_version/Svalboard/data/'
    path = path+dataSelect.value
    df1 = pd.read_csv(path)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+'WORKED'+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
    yLabels1 = df1.columns.values
    yLabels1 = list(yLabels1[1:])
    minDf1 = pd.to_datetime(df1[df1.columns.values[0]]).min()
    maxDf1 = pd.to_datetime(df1[df1.columns.values[0]]).max()


    path = 'C:/Users/MATEO/Documents/infoTeo/Personal_Projects/Hack_the_Artic/svalboard/data/'+dataSelect2.value
    df2 = pd.read_csv(path)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+'WORKED'+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')
    yLabels2 = df2.columns.values
    yLabels2 = list(yLabels2[1:])
    minDf2 = pd.to_datetime(df2[df2.columns.values[0]]).min()
    maxDf2 = pd.to_datetime(df2[df2.columns.values[0]]).max()

    if minDf1 < minDf2:
        init_date = minDf1
        xData =  list(pd.to_datetime(df1[df1.columns.values[0]]))
    else:
        init_date = minDf2
        xData =  list(pd.to_datetime(df2[df2.columns.values[0]]))

    if maxDf1 > maxDf2:
        final_date = maxDf1
        xData =  list(pd.to_datetime(df1[df1.columns.values[0]]))
    else:
        final_date = maxDf2
        xData =  list(pd.to_datetime(df2[df2.columns.values[0]]))
    #init_date = pd.to_datetime(df['Unnamed: 0']).values.min()
    #final_date = pd.to_datetime(df['Unnamed: 0']).values.max()
    date_range_slider = DateRangeSlider(value=(init_date, final_date),
                                    start=init_date, end=final_date)
    date_range_slider.on_change("value", update)

    yAxis = Select(title='Feature', value=yLabels1[0], options=yLabels1)
    yAxis.on_change('value', update)

    yAxis2 = Select(title='Feature', value=yLabels2[0], options=yLabels2)
    yAxis2.on_change('value', update)

    plot = make_plot()

    # set up layout
    inputs = column(dataSelect, yAxis,dataSelect2, yAxis2,unitsLabel,date_range_slider)
    layout = row(inputs, plot, width=2000)

    #layout = row(inputs, plot, width=800)
    tab = Panel(child = layout, title = 'Climate Data')
    return tab
