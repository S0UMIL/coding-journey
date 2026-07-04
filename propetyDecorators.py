class Employee:
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
    @property
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(' ')
        self.first=first
        self.last=last
    @fullname.deleter
    def fullname(self):
        print("NAME DELETED!")
        self.first=None
        self.last=None
    @property
    def email(self):
        return'{}.{}@x.com'.format(self.first,self.last)
emp_1=Employee('Soumil','Tiwary','50000')
#using property decorators allows our attributes "getter" , "setter" and "deleter"
#take an instance where we changed the name of an employee
emp_1.first='rishu'
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
#from the output we notice that the first name only changed/updated for fullname and first but not email
#so what if we want to update the email too how do we do that ? by creating another method of email and removing it as an attribute
#it works. but what if other people are using this they would have to manually change the class and everything so we need to find another way
#we can use "@property" method which can remove the problem of adding parethesis everywhere like see above
#works
#now suppose i change fullname.
emp_1.fullname='Virat Kohli'
print(emp_1.first)
print(emp_1.fullname)
print(emp_1.email)
#we would want to update the email the first and last name too right now we cant do this
#to solve this problem we will have to use an setter
#works.
#we can also make an deleter in an sameway if we wanted to remove some fullname of an employee
del emp_1.fullname
#thats it