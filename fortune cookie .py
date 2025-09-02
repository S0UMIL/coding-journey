import random

def fortune():
  i = random.randint(1,9)
  if i==1 :
    print('Don''t pursue happiness – create it.')
  elif i==2 :
    print('All things are difficult before they are easy.')
  elif i==3 :
    print('The early bird gets the worm, but the second mouse gets the cheese.')
  elif i==4 :
    print('Someone in your life needs a letter from you.')
  elif i==5 :
    print('Don''t just think. Act!')
  elif i==6 :
    print('Your heart will skip a beat.')
  elif i==7 :
    print('The fortune you search for is in another cookie.')
  else:
    print('Help! I''m being held prisoner in a Chinese bakery!')

fortune()
