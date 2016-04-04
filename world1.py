#Lyndsey Craig and Vincent Duarte
#Annual Freshwater Withdrawals data visualization project

#imports the pygal library, which helps create maps and charts
import pygal
from pygal.style import Style

#style customization
custom_style = Style (
  background= '#000000',
  plot_background= 'transparent',
  foreground= '#53E89B',
  foreground_strong= '#53A0E8',
  foreground_subtle= '#ffffff',
  opacity= '1',
  opacity_hover= '.9',
  transition= '400ms ease-in',
  #colors for countries
  colors= ('#BA55D3', '#7B68EE', '#0099FF', '#00FF66', '#0066FF', '#ffffff', '#00FF00', '#FF00FF', '#ffff66', '#00FA9A', '#0000FF'))

#generates map with our custome style sheet
worldmap_chart = pygal.maps.world.World(style=custom_style)
#gives the map a title
worldmap_chart.title = 'Annual Freshwater Withdrawals for 2013 (in billion cubic meters)'
#adds a category to the map with each country that falls under it
worldmap_chart.add('Less than .1', {
  	'mc': 0.0, 'mv': 0.0, 'st': 0.0, 'sc': 0.0,
  	'gq': 0.0, 'dj': 0.0, 'ls': 0.0, 'cg': 0.0,
  	'mt': 0.0
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('0.1-0.99', {
    'mt': 0.1, 'lu': 0.1, 'cf': 0.1, 'gm': 0.1,
    'bn': 0.1, 'bz': 0.1, 'bj': 0.1, 'lr': 0.1,
    'ga': 0.1, 'rw': 0.2, 'me': 0.2, 'is': 0.2,
    'tg': 0.2, 'gw': 0.2, 'cy': 0.2, 'sg': 0.2,
    'bw': 0.2, 'sl': 0.2, 'na': 0.3, 'bi': 0.3,
    'ug': 0.3, 'ba': 0.3, 'bt': 0.3, 'bh': 0.4,
    'pg': 0.4, 'lv': 0.4, 'mn': 0.6, 'gn': 0.6,
    'er': 0.6, 'sr': 0.6, 'hr': 0.6, 'dk': 0.7,
    'cd': 0.7, 'sk': 0.7, 'ao': 0.7, 'mu': 0.7,
    'ie': 0.8, 'bf': 0.8, 'td': 0.9, 'mz': 0.9,
    'kw': 0.9, 'jm': 0.9, 'jo': 0.9, 'si': 0.9
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('1-4.99', {
	'cm': 1.0, 'gh': 1.0, 'ne': 1.0, 'pr': 1.0,
    'mk': 1.0, 'pa': 1.0, 'sz': 1.0, 'md': 1.1,
    'tl': 1.2, 'ht': 1.2, 'lb': 1.3, 'al': 1.3,
    'om': 1.3, 'mr': 1.4, 'mw': 1.4, 'gy': 1.4,
    'ni': 1.5, 'ci': 1.5, 'zm': 1.6, 'hn': 1.6,
    'fi': 1.6, 'cz': 1.7, 'ee': 1.8, 'ge': 1.8,
    'il': 2.0, 'bo': 2.1, 'sv': 2.1, 'kh': 2.2,
    'sn': 2.2, 'cr': 2.4, 'lt': 2.4, 'py': 2.4,
    'ch': 2.6, 'se': 2.6, 'ke': 2.7, 'tn': 2.9,
    'no': 2.9, 'am': 2.9, 'so': 3.3, 'gt': 3.3,
    'la': 3.5, 'ye': 3.6, 'at': 3.7, 'uy': 3.7,
    'ae': 4.0, 'rs': 4.1, 'zw': 4.2, 'ly': 4.3,
	'by': 4.3, 'cu': 4.4, 'nz': 4.8
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('5-9.9', {
    'tz': 5.2,'ml': 5.2, 'do': 5.5, 'et': 5.6,
    'hu': 5.6,'dz': 5.7, 'bg': 6.1, 'be': 6.2,
    'ro': 6.9,'kg': 8.0, 'pt': 8.5, 'kp': 8.7,
    'gl': 9.5,'np': 9.5, 'ec': 9.9
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('10-19.99', {
    'nl': 10.6,'my': 11.2,
    'tj': 11.5, 'co': 11.8, 'pl': 12.0, 'az': 12.0,
    'za': 12.5, 'ma': 12.6, 'lk': 13.0, 'gb': 13.0,
    'ng': 13.1, 'pe': 13.7, 'mg': 16.5, 'sy': 16.8,
	'ua': 19.2
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('20-29.99', {
    'af': 20.3, 'kz': 21.1, 'au': 22.6,
    've': 22.6,	'sa': 23.7, 'kr': 25.5, 'sd': 26.9,
    'tm': 28.0
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('30-39.99', {
    'fr': 31.6, 'de': 32.3, 'es': 32.5,'mm': 33.2,
    'cl': 35.4, 'bd': 35.9, 'ar': 37.8,
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('40-49.99', {
    'tr': 40.1, 'ca': 42.2, 'it': 45.4
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('50-99.9', {
    'uz': 56.0, 'th': 57.3, 'iq': 66.0, 'ru': 66.2,
    'eg': 68.3, 'br': 74.8, 'mx': 80.3, 'ph': 81.6,
    'vn': 82.0, 'jp': 90.0, 'ir': 93.3
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('100-200', {
	'id': 113.3, 'pk': 183.5,
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('200+', {
	'us': 478.4, 'cn': 554.1, 'in': 761.0
	})

#creates map
worldmap_chart.render_to_file('worldmap_waterUsage.svg')