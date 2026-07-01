#regular class methods in a class automatically take the first instance as the first arguement
#by convention we were calling this as "self"
#how can we change this so that it automatically takes the class as the first argument? to do that we are gonna use class methods
#to convert an regular method as an class method you add an decorator - "@classmethod"
# now we r gonna be using the previous code too here for explaination
class Employe:
    num_of_emps=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@x.com'
        Employe.num_of_emps +=1 
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod#decorator is basically altering the functionality of our method to where now we receive the class as our first arguement
    def set_raise_amt(cls,amount):#by convention we use cls just like how we used self for class as first instance we use cls here
        cls.raise_amount=amount

    @classmethod
    def from_str(cls,emp_str):
        first , last , pay =emp_str_1.split('-')
        return cls(first,last, pay)#this line will create tht new employee
    
    @staticmethod
    def is_workday(day):
        #in python we have this methods where Monday=0 and Sunday=6
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


emp_1=Employe('Soumil','Tiwary',5000)
emp_2=Employe('Sheru','Singh',1000)
Employe.set_raise_amt(1.05)#it automatically accepts the class so we dont have to pass that in, so we directly just pass the amount
print(Employe.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#after running we notice all of them are 1.05 meaning 5% notice how in this case we dint specify the self or any instance the whole thing got applied to every instance in tht class bcuz we were working with the class-methods
# what if we try running a instance.classmethod wil it work ? well yes it does but again it will apply to all instances not just tht instance
emp_1.set_raise_amt(1.05)
print(Employe.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#again all outputs are 1.05...
#okay moveing on , creating an employee instance becomes hectic what if there was an simple way to just enter the string of the specfic requirements and that became a instance
#creating example-
emp_str_1='John-Bhai-70000'
emp_str_2='Steve-Smith-30000'# so imagine this a user wants the instance to be made just by this
emo_str_3='Jana-Bhai-90000'
#so how do we reverse engineer this to users liking for creating instances? first we split the information given
###first , last , pay = emp_str_1.split('-')
###new_emp1= Employe(first,last,pay)
###print(new_emp1.email)
###print(new_emp1.pay)
#we notice it works just fine and similar to other emps we made
#but this this again too hectic for them to create again and again so what do we do lets just create an classmethod for this too
#creating new class method above on line 25
#now instead of typing all tht blabber we have provided them an method through which they just have to type this 
new_emp_1= Employe.from_str(emp_str_1)
print(new_emp_1.email)
print(new_emp_1.pay)
#as expected still works, we have succesfully provided them with an alternative constructor now they can just pass in their own strings and get their employee objects
#now coming to static methods
#just how we observed for class methonds we passed in cls automatically and for instances we did self . for static we dont pass anything
#they behave like regular functions but its just that we include them in our classes because they have some logical connection with the class
#for example we want to create an method which returns if that specfic date is an working day or not now this is logically connected to the above class but doesnt depend on any instance or class variable
#go above we will now create staticmethod
import datetime
my_date=datetime.date(2026,7,1)
print(Employe.is_workday(my_date))
#there u go ur static method works.
