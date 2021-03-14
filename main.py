# Pandas for data management
import pandas as pd

# os methods for manipulating paths
import os
# Bokeh basics
from bokeh.io import curdoc
from bokeh.models.widgets import Tabs

#Each tab is drawn by one script
from scripts.weather  import weather_tab
from scripts.pollutans import pollutans_tab
from scripts.svalbard_map import svalbard_map_tab

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+dir_path+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')

#Load data sets
#datapath = os.path.join("data", "")
#datapathICOS = ".\\data\\ICOS_ATC_L2_L2-2020.1_ZEP_15.0_CTS."

#df = pd.read_csv(r'C:\Users\MATEO\Documents\infoTeo\Personal_Projects\Hack_the_Artic\svalboard\carbon_data.csv')
#print('!!!!!!!!!!!!!!!!!!!!!!!!!! '+'WORKED'+' !!!!!!!!!!!!!!!!!!!!!!!!!! ')

icosCO2_df =1# pd.read_csv(r"data\ICOS_ATC_L2_L2-2020.1_ZEP_15.0_CTS.CO2", header=40, sep=';')
icosCO_df =1 #pd.read_csv(r"data\ICOS_ATC_L2_L2-2020.1_ZEP_15.0_CTS.CO", header=40, sep=';')
icosCH4_df =2 #pd.read_csv(r"data\ICOS_ATC_L2_L2-2020.1_ZEP_15.0_CTS.CH4", header=40, sep=';')
icosMTO_df =1 #pd.read_csv(r"data\ICOS_ATC_L2_L2-2020.1_ZEP_15.0_CTS.MTO", header=35, sep=';')

# Create each of the tabs
tab1 = weather_tab(icosMTO_df)
#tab2 = pollutans_tab(icosCO_df,icosCO2_df,icosCH4_df)
tab3 = svalbard_map_tab(icosMTO_df)

# Put all tabs in the application
curdoc().theme = 'dark_minimal'
tabs = Tabs(tabs = [tab3, tab1])
curdoc().add_root(tabs)
