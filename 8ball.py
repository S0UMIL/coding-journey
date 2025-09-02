import random
question = input('Question:')
random_number = random.randint(1,9)
if random_number == 1:
  print('Yes defintely')
elif random_number == 2:
  print('it is decidely so')
elif random_number == 3:
  print('without a doubt')
elif random_number == 4:
  print('reply hazy , try again')
elif random_number == 5:
  print('ask again later')
elif random_number == 6:
  print('better not tell you now')
elif random_number == 7:
  print('my sources say no')
elif random_number == 8:
  print('outlook not so good')
else:
  print('very doubtful')
