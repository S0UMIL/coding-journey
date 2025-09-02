items = ['🍔 Cheeseburger' ,'🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']
def welcome():
  print('what would u like to have today')
  return items
def get_items():
  Order = int(input('enter the value of spefic food item - '))
  if Order > 4 :
    print('error')
  else:
    print('thank you for choosing MCD', 'here''s food', items[Order] ,' that u ordered')
  return Order
welcome()
get_items()
