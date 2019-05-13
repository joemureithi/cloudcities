class City(object):
    """Class to represent a city object

    Attributes:
            name(str): Name of the city.
            iscode(str): The country ISO alpha-2 code
            latitude(float): Latitude in degrees
            longitude(float): Longitude in degrees
            cloud(int): Cloud cover percentage. Will default to zero if not specified.
    """
    def __init__(self, name, isocode, lat, lon, cloud=0):
        """City init method

        """
        self.name = name
        self.isocode = isocode
        self.lat = lat
        self.lon = lon
        self.cloud = cloud

    def get_name(self):
        return self.name
    
    def get_isocode(self):
        return self.isocode

    def get_lat(self):
        return self.lat
    
    def get_lon(self):
        return self.lon

    def get_cloudcover(self):
        return self.cloud

