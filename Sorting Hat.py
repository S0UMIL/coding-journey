# Write code below 💖
g=0
r=0
s=0
h=0
Q1=int(input('Do you like (1)Dawn (2)Dusk:-'))
if Q1==1:
  g +=1
  r +=1
elif Q1==2:
  h +=1
  s +=1
else:
  print('Wrong input')
Q2=int(input('When I''m dead,I want people to remember me as (1)The Good (2)The Great (3)The wise (4)The Bold:-'))

if Q2==1:
  h +=2
elif Q2==2:
  s +=2
elif Q2==3:
  r +=2
elif Q2==4:
  g +=2
else:
  print('wrong input')
Q3=int(input('Which kind of instrument more pleases your ear (1)The violin (2)The trumpet (3)The piano (4)The drum:-'))

if Q3==1:
  s +=4
elif Q3==2:
  h +=4
elif Q3==3:
  r +=4
elif Q3==4:
  g +=4
else:
  print('wrong input')
if h > g and h > s and h > r:
  print('Hufflepuff it is!!!!')
if g > h and g > s and g > r:
  print('Gryffindor for sure !!!')
if s > h and s > g and s > r:
  print('Slytherin suits you well !!!')
if r > h and r > g and r > s:
  print('Ravenclaw shall help you fly!!!')


