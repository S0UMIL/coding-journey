#Python Obejct Oriented Programming
#Why use classes? they allow us to logically group our data and functions in a way thats easy to reuse and also easy to build upon if needed
#method --> function assiociated with tht class
class Employee:
    pass
#if you ever have an class which u wanna leave empty for the time being then simply use "pass"
#creating instances
empy_1=Employee()
empy_2=Employee()
#here employee 1 and 2 are instances of the class employee
#instance variables contain data that is unique to each instance
#creating instance variables
empy_1.first='Soumil'
empy_1.last='Tiwary'
empy_1.email='soumil.tiwary@x.com'
empy_1.pay=0

empy_2.first='Sheru'
empy_2.last='Singh'
empy_2.email='sheru.singh@x.com'
empy_2.pay=10000

print(empy_1.email)
print(empy_2.email)
#so notice how we created sm variables are information for employees manually? this on a large scale can be very tedious and prone to error
#so to make them setup automatically we shall be using the __init__ method which bascially means intialize
#THE ABOVE CODE IS FOR UNDERSTANDING THE USE CASE DIFFERENT CLASS AND INSTANCES WILL BE USED BELOW FOR FUTHER DEMO
class Employe:
    def __init__(self,first,last,pay):
        #setting up all the instance variables
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last + '@x.com'
    #this specifc part comes later line 52 onwards
    def fullname(self):
        return'{} {}'.format(self.first,self.last)
#when we create methods within the class they receive the instance as the first arguement automatically by convention its 'SELF'
#so now when we try creating instances for our employe class right here now we can pass the values that we specified in our init method
#now our init method takes self,first,last,pay as arguements but when we create employee down here the instance is passed automatically
#meaning we dont need to mention self in every instance since its passed automatically
emp_1=Employe('Soumil','Tiwary',0)
emp_2=Employe('Sheru','Singh',1000)
print(emp_1.pay)
print(emp_2.pay)
#keep in mind while making an instance we need to keep arguements in order. ie self , first , last , pay
#now because of this that entire manual task above is gone with so many lines of code saved
#now lets say we wanted to pertfom some kind of action to do that we can add methods to our class
#lets say we want to show the full name of the employee
#one option is we can do this manually by simply
print('{} {}' .format(emp_1.first,emp_1.last))
#but this is alot to type in each time u want to show some employees full name
#2nd option so lets create an method inside our class that allows us to use it like an function
#see line 37 we simply created a function of printing a fullname now its not gonna be a labours task keep in mind this is called an method
print(emp_1.fullname())
#notice that we will be needing parenthesis here after fullname that is because this is an method not an attribute like first,last,pay
#important error- what if from the method fullname i did not mention self inside as an arguement? well its obvivously an error but 
#if you dont do any operation as in call the menthod like we did on line 55 there wont be any error the code will run just fine
#this is where many people get confused and miss on the this tiny detail
#but if u do call it like we did in line 55 it will show an error - TypeError:fullname() takes 0 positional value but 1 was given
#thats it for today
