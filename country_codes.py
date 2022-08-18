from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country_name):
    """Return 2 digit country code for a given country name"""
    
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country was not found return none
    return None

    