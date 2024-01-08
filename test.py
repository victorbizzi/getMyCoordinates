import geocoder
#Currenly I am trying to improve this code to access the GPS COM/Port/Serial to get the exact coordinates

def get_coord(s_name):
    if s_name == 'ipinfo':
        g = geocoder.ipinfo('me')
    elif s_name == 'freegeoip':
        g = geocoder.freegeoip('me')
    else:
        return None, "Service not working good"

    if g.ok:
        return g.latlng, None
    else:
        return None, g.error

services = ['ipinfo', 'freegeoip']
for service in services:
    location, error = get_coord(service)
    if location:
        print(f"Coordinates: {location}")
        break
    else:
        print(f"Error: {service}. Log - {error}")

if not location:
    print("FAIL")