import random

symbols = [' 🍒', '🍇' ,' 🍉', '7️⃣']
result_1 = random.choices(symbols, k=3)


print(f'{result_1[0]} | {result_1[1]} | {result_1[2]}')
if result_1[0] == '7️⃣'  and result_1[1] == '7️⃣' and result_1[2] == '7️⃣':
  print('jackpot')
else:
  print('thanks for playing')
