#we wil be implementing special methods within our classes called magic methods
#this allows us to emulate some built-in behavior within python and also how we implement operator overloading
#in python when we do
print(1+2)#we get an integer
#but when we do
print('a'+'b')#it just concatnates
#now similarly when we try to printout our employee instance here like employee one or 2 we get an unique address or something
#what if we would want to change that , what it prints how it prints etc.
class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@x.com'
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)
    def __repr__(self):
        return "Employee('{}','{}','{})".format(self.first,self.last,self.pay)
    def __str__(self):
        return '{} -- {}'.format(self.fullname(),self.email)
    def __add__(self,other):#we will be using 2 attributes since there are 2 employees other is an convention
        return self.pay + other.pay 
    def __len__(self):
        return len(self.fullname()) 
##previous code which we have been using
#double underscores are called dunder dunder init == __init__
#so dunder init is an special method which we have been using , its the first and most common dunder method used
#SOME OTHER COMMON DUNDER METHODS - dunder repr and dunder str
#repr--> supposed to be an unambigous representation of the object and should be used for debugging logging and things like that.
#str--> is meant to be more readable representation of an object and is meant to be used as a display to the end user
emp_1=Employee('Soumil','Tiwary',5000)
emp_2=Employee('Sheru','Singh',1000)
#print(emp_1)#for this u get an output of an object some random nums n stuff
#repr(emp_1)#here u get as u formatted above clean and simple note u will get this after typing print statement like its essentially formatting that 
#now lets define str .. when we comment out repr and just run print we will notice that the format is exactly how it was in str without even doing something like str(emp_1)
#print(repr(emp_1))
#print(str(emp_1))
#print(emp_1.__repr__())
#print(emp_2.__str__())
#all of these print the samething
#lets explore a few more special methods - dunder add , used for adding stuff letters, strs, numbers etc
#now lets program this in such a way that i add my employees and it returns the sum of their pay
#lets comment out everything to check our dunder add condition works or no
#print(emp_1 + emp_2)
#works
#the len function we used commonly for finding length of an string is also an dunder method lets use it to find length of fullname of employees
#commenting out everything else 
print(len(emp_1))
#works