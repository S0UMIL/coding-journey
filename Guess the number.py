guess = 0
tries = 0
while guess !=6 and tries < 5:
  guess = int(input('guess the number:'))
  if tries >= 5:
    print('out of tries')
  tries +=1
print('you got it!')
