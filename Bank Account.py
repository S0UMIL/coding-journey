balance=10000

class BankAccount: 
  def __init__(self, first_name, last_name, account_id, account_type , pin , balance):
    self.first_name = first_name
    self.last_name = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
Soumil = BankAccount('Soumil','Tiwary',123456789,'savings', 0000, balance)
def deposit(self):
  x = 96
  self.balance += x
  print(self.balance ,'$  amount is left in your account')
  return (self.balance)
def withdraw(self):
  a = 25
  self.balance -= a
  print(self.balance , '$ amount is left in your account')
  return(self.balance)
def display_balance(self):
  print('your current balance is :-' , self.balance )
  return(self.balance)


deposit(Soumil)
withdraw(Soumil)
display_balance(Soumil)
