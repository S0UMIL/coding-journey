height=int(input('please enter you height in cms'))
credit=int(input('please enter how many credits you have'))
if height >=137 and credit >=10:
  print('Enjoy the ride')
if height >=137 and credit < 10:
  print('you dont have enough credits')
if height <137 and credit >=10:
  print('you are not tall enough')
if height <137 and credit < 10:
  print('you have not met the requirements')
