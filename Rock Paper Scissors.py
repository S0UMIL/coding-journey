import random
R=('R')
P=('P')
S=('S')
print('Hello, lets play rock paper scissors')
i=(input('Choose rock paper or scissors: '))
computer = random.choice([R , P , S])
print('computer chose:', computer)
if i== R and computer== P:
 print('✊ VS ✋ , you lose')
elif i== R and computer== S:
  print ('✊ VS ✌️ , you Win')
elif i== P and computer== R:
  print ('✋ VS ✊ , you win')
elif i== P and computer== S:
  print ('✋ VS ✌️, you lose')
elif i== S and computer== P:
  print ('✌️ VS ✋ , you win')
elif i== S and computer== R:
  print ('✌️ VS ✊, you lose')
else:
  print('its a tie')
