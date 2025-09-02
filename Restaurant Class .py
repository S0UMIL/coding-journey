class Restaurant:
  name =''
  category =''
  rating = 0
  delivery = False
bobs_burgers = Restaurant()
ishans_dhaba = Restaurant()
raghav_momo_wala = Restaurant()
bobs_burgers.name = 'bob''s burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False
ishans_dhaba.name = 'ishan''s dhaba'
ishans_dhaba.category = 'Indian'
ishans_dhaba.rating = 5
ishans_dhaba.delivery = True
raghav_momo_wala.name ='raghav momo wala'
raghav_momo_wala.category = 'chinese'
raghav_momo_wala.rating = 4.9
raghav_momo_wala.delivery = False
print(vars(bobs_burgers))
print(vars(ishans_dhaba))
print(vars(raghav_momo_wala))
