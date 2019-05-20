# cloudcities
Python program to retrieve and map cloud coverage in cities from OpenWeatherMap web API

# Setup
* Requires Python 3.6 and above.
* Clone this repo https://github.com/joemureithi/cloudcities.git
* Create the environment using the *environment.yml* file: conda env create -f environment. yml

# Data and resources
* Uses a list of cities in a shapefile obtained from https://www.naturalearthdata.com/downloads/10m-cultural-vectors/10m-populated-places/ . The shapefile has been modified using the *data_preparation.py* to include a continent field.
* Requires an access token to retrieve weather data from OpenWeather API.

# Run
Open and run *cloudcities.ipynb* Jupyter notebook.
