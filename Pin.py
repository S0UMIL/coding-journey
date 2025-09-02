print('Bank of codex')

pin = int(input('enter you PIN:'))

while pin !=1234:
  pin = int(input('incorrect pin.enter your pin again:'))

if pin == 1234:
  print('pin accepted!')
