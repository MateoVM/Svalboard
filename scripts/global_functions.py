import numpy as np

# Convert Latitude and Longitude to mercator map projections

def latlon_to_mercator(lat, lon):
    latitude = lat # (φ)
    longitude = lon # (λ)
    mapWidth = 200
    mapHeight = 200
    # get x value
    x = (longitude+180)*(mapWidth/360)
    #convert from degrees to radians
    latRad = latitude*np.pi/180
    # get y value
    mercN = np.log(np.tan((np.pi/4)+(latRad/2)))
    y = (mapHeight/2)-(mapWidth*mercN/(2*np.pi))
    return [x,y]
    #output_file("gmap.html")
    #output_file("svalbard.html")
    # MERCATOR
    #tile_provider = get_provider(CARTODBPOSITRON)

    # range bounds supplied in web mercator coordinates
    #location=[78.698105, 15.723717]
    # x,y points on mercator map projections
    #coor = latlon_to_mercator(location[0], location[1])
    #mapSvalbard = figure(x_range=(coor[0]-100, coor[0]+100),
    #y_range=(400, coor[1]+100),
    #mapSvalbard = figure(x_range=(2000, 4000),
    #y_range=(2000, 4000),
    #x_axis_type="mercator", y_axis_type="mercator")
    #mapSvalbard.add_tile(tile_provider)
