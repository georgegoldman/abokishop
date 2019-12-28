import geocoder

class Geolocation:

    city = geocoder.ipinfo('me').city
    state = geocoder.ipinfo('me').state
    country = geocoder.ipinfo('me').country

    def __init__(self):
        self.city
        self.country

    def __repr__(self):
        return f"['{self.city}']"
        