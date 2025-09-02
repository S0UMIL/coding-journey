import datetime , bday_messages
todays_date = datetime.date.today()
print(todays_date,'is todays date')
next_birthday = datetime.date( 2026,8,23)
print(next_birthday , 'is your birthday')
days_away =   next_birthday - todays_date 
print('days remaining for your bday',days_away)
if todays_date == next_birthday:
    print(random_message)
else:
    print(f'my birthday is {days_away} away')
