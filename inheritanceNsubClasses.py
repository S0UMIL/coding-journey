#inheritance allows us to inherit attributes and methods from a parent class this is useful because we can create subclasses
#we can get all of the functionality of the parent class then we can overwrite or add completely new functionality without affecting the parent class
#again taking the employee example lets just say we wanted to create different types of employees
#lets say we want to create developers and managers now these would be suitable for subclasses bcuz they come under the employee logically makes sense

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
class developer(Employee):#here we are telling the developer class to inherit the employee class
    raise_amount=1.10
    def __init__(self,first,last,pay,prog_Lang):#now without any code too the developer class will have all the attributes and methods of our employee class
        super().__init__(first,last,pay)#what we are doing here is telling the system that let the employee class handel the first last and pay
        #we can also do Employee().__init__(self,first,last,pay) this is necessary when having multiple inheritence
        self.prog_Lang=prog_Lang

class manager(Employee):
    raise_amount=1.15
    def __init__(self,first,last,pay,position):
        super().__init__(first,last,pay)
        self.position=position
          
dev_1=developer('kobe','bryant',50000,'python')#you can replace this with developer now , what happens here first the system searches the entire developer class after it finds nothing it goes to its inheritance until it finds what its looking for now this chain is called method resolution order 
dev_2=developer('shaq','oneil',70000,'java')
print(dev_1.email)
print(dev_2.email)
#okay now lets say we wanted to customize our developer subclass a little bit
#lets say we want to change the raise amount to 10% we can do that in the subclass itself it will overwrite whatever similar condn is present in the employee class
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
#it works
#coming to some complicated stuff sometimes we want to initate our sub classes with more information than our parent class can handle
#lets say when we created our developers here we want to show their main programming language as an attribute too
# now since we only have 3 attriubutes to employees and we specifcally want something in developer as an new attribute what we are gonna do is create an init method inside of the developer class 
#checking if out init method on the inheritance is working or not
print(dev_1.prog_Lang)
print(dev_2.prog_Lang)
#now let us create another subclass called manager
man_1=manager('mohan','sharma',90000,'AVP')
man_2=manager('saurav','jha',100000,'VP')
print(man_1.pay)
print(man_2.pay)
print(man_1.position)
#now python has these 2 functions called is instance , is subclass it will tell us if an object is an instance of a class.
print(isinstance(man_1,Employee))
print(issubclass(manager,Employee))
#done everything works