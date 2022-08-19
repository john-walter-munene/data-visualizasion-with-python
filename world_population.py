import json
from tkinter.ttk import Style
import pygal_maps_world.maps as pwm
from pygal.style import RotateStyle, LightColorizedStyle

from country_codes import get_country_code

# Load data into a list.
file_name = 'population_data.json'
with open(file_name) as f:
    pop_data = json.load(f)
    
# Print the 2010 population for each country.
# Build a dictionary of population data
cc_population = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # Convert strings into numerical values
        population = int(float(pop_dict['Value']))
        country_code = get_country_code(country_name)
        if country_code:
            cc_population[country_code] = population
            print(f"{country_code} : {str(population)}")
        else:
            print("Error -" + country_name)
            
# Grouping the countries into 3 population levels
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
    if pop < 100000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
        
# See how many countries are in each level
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
            
wm = pwm.World()

# Styling the map
wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
wm = pwm.World(Style==wm_style)

# Defining the map attributes
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
 
wm.render_to_file('world_population.svg')
    