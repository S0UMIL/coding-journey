from math import pi
from random import choice as ch
planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]
random_planet = ch(planets)
print(random_planet)
r=0


if random_planet =='Mercury' : 
  r = 2440
  print(r)
elif random_planet =='Venus':
  r = 6052
  print(r)
elif random_planet == 'Earth':
  r = 6371
  print(r)
elif random_planet =='Mars':
  r = 3390
  print(r)
elif random_planet =='Saturn':
  r = 58232
  print(r)
else:
  print('Oops an error has occured')
Area = 4 * pi * (r ** 2)
