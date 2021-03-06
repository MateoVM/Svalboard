import numpy as np
import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column, row, WidgetBox
#from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

from bokeh.models import (CategoricalColorMapper, HoverTool,
						  ColumnDataSource, Panel,
						  FuncTickFormatter, SingleIntervalTicker, LinearAxis,
                          TextInput)

from bokeh.models.widgets import (CheckboxGroup, Slider, RangeSlider,
								  Tabs, CheckboxButtonGroup,
								  TableColumn, DataTable, Select)

from bokeh.palettes import Category20_16


def pollutans_tab(CO_data, CO2_data, CH3_data):
    # Set up data
    N = 200
    x = np.linspace(0, 4*np.pi, N)
    y = np.sin(x)
    source = ColumnDataSource(data=dict(x=x, y=y))


    # Set up plot
    plot = figure(plot_height=400, plot_width=400, title="my sine wave",
                  tools="crosshair,pan,reset,save,wheel_zoom",
                  x_range=[0, 4*np.pi], y_range=[-2.5, 2.5])

    plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)


    # Set up widgets
    text = TextInput(title="title", value='my sine wave')
    offset = Slider(title="offset Pollutans", value=0.0, start=-5.0, end=5.0, step=0.1)
    amplitude = Slider(title="amplitude Pollutans", value=1.0, start=-5.0, end=5.0, step=0.1)
    phase = Slider(title="phase Pollutans", value=0.0, start=0.0, end=2*np.pi)
    freq = Slider(title="frequency Pollutans", value=1.0, start=0.1, end=5.1, step=0.1)


    # Set up callbacks
    def update_title(attrname, old, new):
        plot.title.text = text.value

    text.on_change('value', update_title)

    def update_data(attrname, old, new):

        # Get the current slider values
        a = amplitude.value
        b = offset.value
        w = phase.value
        k = freq.value

        # Generate the new curve
        x = np.linspace(0, 4*np.pi, N)
        y = a*np.sin(k*x + w) + b

        source.data = dict(x=x, y=y)

    for w in [offset, amplitude, phase, freq]:
        w.on_change('value', update_data)


    # Set up layouts and add to document
    inputs = column(text, offset, amplitude, phase, freq)

    #curdoc().add_root(row(inputs, plot, width=800))
    #curdoc().title = "Sliders"
    layout = row(inputs, plot, width=800)
    tab = Panel(child = layout, title = 'Pollutans')

    return tab
