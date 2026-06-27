#Class variables are variables that are shared among all instances of a class
#instance variables can be unique like our names , email etc. class variables should be the same for each variable
#for this particular code lets use an example like an company giving annual raises to their employees , amount can change year by year
#but the amount remains the same for all employees
class Employe:
    num_of_emps=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        #setting up all the instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@x.com'
        Employe.num_of_emps +=1 #whenever we create a new profile its always done using this framework so adding this in the end will make sure count is updated
        #over here we dint use self.nums_of_emps because there is no case where would want an instance value to be more than the class in this scenario
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
    #lets first hardcode this 
    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)#bonus is basically 4%

emp_1=Employe('Soumil','Tiwary',5000)
emp_2=Employe('Sheru','Singh',1000)
print(emp_1.pay)#first printing the base pay
emp_1.apply_raise()#applying/adding bonus
print(emp_1.pay)#printing the bonus +pay
#heres the flaw about this method what if i want to change the % of bonus or view the % of bonus its complicated
#we wouldnt wanna manually load in and change the bonus % from everywhere.
#so lets pull this 4% out of this class variable , we can simply do that by going to the top of the class and adding raise_amount = smthing
#what if we keep this class variable "raise_amount" in apply_raise like simply replace it by 1.04 bcuz 1.04=apply_raise right?
#if we do this we get an "Name error" saying raise_amount is not defined
#thats bcuz when we access these class variables we either need to access them through the class itself or an instance of the class
#so wht do we do ? we can work by using "employe.raise_amount" OR we can also access through the instance "self.raise_amount"
print(Employe.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#we notice the value of these 3 are the same meaning i can access these class variables from both my class itself and as well as from both instances
Employe.raise_amount=1.05
#here we are changing the raise amount
print(Employe.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
#notice how all the raise_amount became 1.05. it changed the raise amount for both the class and the instances
#now what if i do the same but for a specfic instance?
emp_1.raise_amount=1.06
print(Employe.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# we notice that the change did not effect the whole class but only the instance
#why does this happen? bcuz the attribute was actually created for that specfic instance when we did it for the class the whole class observed change
#so its important that in line 18 we leave it as "self.raise_amount" that gives us the ability to change that amount for a single instance if we want to


#now lets take anothe example of an class variable where keeping self.smtg would not make sense
#lets say we want to keep track of how many employees we have lets create and variable named- num_of_emps
print(Employe.num_of_emps)



