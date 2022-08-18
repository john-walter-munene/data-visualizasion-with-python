import pygal
import pygal_maps_world.maps as pwm

wm = pwm.World()
wm.title = 'Populations of countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')

