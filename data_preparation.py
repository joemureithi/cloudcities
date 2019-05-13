import os, sys, random, country_converter
from osgeo import gdal,ogr

#Clear Console
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()

# Module to match iso codes to continent names
cc = country_converter.CountryConverter()

# Load Cities shapefile in write mode
driver = ogr.GetDriverByName('ESRI Shapefile')
cityds = driver.Open("./cities/cities.shp", update = 1)

if cityds is None:
    print ("Open failed.\n")
    sys.exit( 1 )
else:
    print("File opened")

layer = cityds.GetLayer()

# Update the continent field using country_converter
for feature in layer:
    isocode = [feature.GetField("ISO_A2")]
    continent = cc.convert(isocode, to='continent')
    country = feature.GetField("ADM0NAME")
    feature.SetField("CONTINENT", continent)
    layer.SetFeature(feature)
    print(isocode, '\t', country, '\t', continent)

cityds = None