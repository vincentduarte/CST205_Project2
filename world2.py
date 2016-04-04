#Lyndsey Craig and Vincent Duarte
#Annual Freshwater Withdrawals data visualization project

#imports the pygal library, which helps create map and charts
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

worldmap_chart = pygal.maps.world.World(style=custom_style)
worldmap_chart.title = 'Annual Freshwater Withdrawls for 2013 (% of internal resources)'
#adds a category to the map with each country that falls under it
worldmap_chart.add('Less than .1', {
    'cg': 0.02, 'pg': 0.05, 'cf': 0.05, 'lr': 0.07,
    'gq': 0.07, 'cd': 0.08, 'ga': 0.08
  })
#adds a category to the map with each country that falls under it
worldmap_chart.add('0.1-0.99', {
    'is': 0.10, 'sl': 0.13, 'gn': 0.24, 'st': 0.32,
    'cm': 0.35, 'bt': 0.43, 'ao': 0.48, 'co': 0.52,
    'gy': 0.60, 'sr': 0.52, 'bz': 0.66, 'bo': 0.69,
    'pa': 0.76, 'no': 0.77, 'ug': 0.81, 'pe': 0.83,
    'ls': 0.84, 'mz': 0.88, 'ba': 0.93, 'ni': 0.99
  })
#adds a category to the map with each country that falls under it
worldmap_chart.add('1-3.99', {
    'bn': 1.08, 'gw': 1.09, 'bj': 1.26, 'br': 1.32,
    'nz': 1.45, 'tg': 1.47, 'ca': 1.48, 'fi': 1.53,
    'se': 1.53, 'ru': 1.53, 'rw':1.58, 'mn': 1.58,
    'ie': 1.61, 'hr': 1.67, 'hn': 1.77, 'kh': 1.81,
    'la': 1.83, 'my': 1.93, 'zm': 1.96, 'ci': 2.02,
    'py': 2.06, 'cr': 2.08, 'ec': 2.24, 'lv': 2.50,
    've': 2.81, 'bi': 2.86, 'gm': 3.02, 'gt': 3.04,
    'ge': 3.14, 'gh': 3.24, 'mm': 3.31, 'uy': 3.97
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('4-9.99', {
    'cl': 4.00, 'et': 4.56, 'au': 4.59, 'na': 4.68,
    'np': 4.79, 'al': 4.87, 'mg': 4.90, 'si': 5.05,
    'sk': 5.46, 'id': 5.61, 'td': 5.86, 'ng': 5.93,
    'lu': 6.02, 'tz': 6.17, 'dj': 6.33, 'ch': 6.47,
    'bf': 6.54, 'at': 6.65, 'bw': 8.08, 'mw': 8.41,
    'sn': 8.61, 'ml': 8.64, 'gb': 8.99, 'ht': 9.22,
    'jm': 9.87
    })
#adds a category to the map with each country that falls under it
worldmap_chart.add('10-19.99', {
    'dk': 11.00, 'cu': 11.61, 'by': 11.66,
    'cz': 12.92, 'kp': 12.92, 'ar': 12.94, 'ke': 13.21,
    'sv': 13.55, 'pr': 14.01, 'ee': 14.13, 'tl': 14.27,
    'lt': 15.28, 'fr': 15.81, 'ro': 16.26, 'gr': 16.33,
    'kg': 16.36, 'us': 16.98, 'ph': 17.03, 'tr': 17.67,
    'tj': 18.11, 'mk': 19.04, 'mx': 19.63, 'mv': 19.67,
    'cn': 19.70
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('20.99-29.99', {
    'er': 20.79, 'jp': 20.94, 'pt': 22.27,
    'pl': 22.31, 'vn': 22.82, 'cy': 23.59, 'lk': 24.53,
    'it': 24.88, 'th': 25.53, 'do': 26.06, 'mu': 26.35,
    'lb': 27.29, 'za': 27.90, 'ne': 28.10, 'bg': 29.14,
    'es': 29.19
    })
#adds a category to the map with each country that falls under it
worldmap_chart.add('30-99.99', {
    'de': 30.19, 'sg': 31.67, 'kz': 32.85,
    'bd': 34.16, 'zw': 34.30, 'ua': 36.23, 'kr': 39.28,
    'sz': 39.47, 'am': 42.88, 'af': 43.01, 'ma': 43.48,
    'rs': 49.02, 'dz': 50.87, 'be': 51.80, 'in': 52.63,
    'so': 54.97, 'tn': 67.94, 'ir': 72.61, 'hu': 93.05,
    'om': 94.36, 'nl': 96.45
	})
#adds a category to the map with each country that falls under it
worldmap_chart.add('100-199.99', {
    'md': 106.50, 'mt': 106.73, 'jo': 137.96, 'az': 147.50,
    'ye': 169.76, 'iq': 187.50
	})
#adds a category to the map with each country that falls under it
worldmap_chart.add('200-399.99', {
    'sy': 235.00, 'il': 260.53, 'pk': 333.64, 'mr': 337.50,
    'uz': 342.72
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('400-999.99', {
    'ly': 618.00, 'sd': 673.25, 'sa': 986.25,
})
#adds a category to the map with each country that falls under it
worldmap_chart.add('1000+', {
    'tm': 1989.32, 'ae': 2665.33, 'eg': 3794.44, 'bh': 8935.00
	})
#creates map
worldmap_chart.render_to_file('worldmap_waterUsage%.svg')