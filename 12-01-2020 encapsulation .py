#!/usr/bin/env python
# coding: utf-8

# # Encapsulation

# In[15]:


class A():
    def __init__(self, name, age):    #__ means private - no access and no update
        self.__sname = name
        self.__age = age
        
    def display(self):
            print("name:", self.__sname)
            print("age:", self.__age)
            
    def change(self,a,b):
            self.__sname = a
            self.__age = b
            
    def __info(self):
            print("Hello")
            
    def abc(self):
            self.__info()
            
            
obj1 = A("Ali", 25)
#obj1.sname  #Private attribute calling - no access


# In[3]:


obj1._A__sname  #class reference calling


# In[16]:


obj1.display()


# In[17]:


obj1.change("asif", 30)
obj1.display()


# In[18]:


obj1.abc()


# # Abstract

# In[12]:


class A:  #abstract class in python 2.0
    def __init__(self, a, b):
        self.a=a
        self.b=b
        
class B(A):
    pass


# In[25]:


obj1=(2,4)


# In[26]:


print(obj1.a)
print(obj1.b)


# In[28]:


obj2 = B(7, 9)


# In[32]:


from abc import ABC, abstractmethod  #class Capital letter, function small letter
#no direct instance, but used with inheritance

class Human(ABC): #ABC default file called module and has function named as abstractmethod
    #Human child parent ABC
    
    @abstractmethod     #decorator
    def __init__(self):
        self.name=None
        self.age=None
    
     
    def display(self, name, age):
        self.name=name
        self.age=age
        return "Object name is {} {} old.".format(self.name, self.age)
    

p1=Human() #error generate because 
p1.display('Ali', 25)


# In[35]:


class Male(Human):
    
    def __init__(self):
        self.name='Ali'
        self.fname='ABC'
    def laughter(self):
        return 'HAHAHA'
p1=Male()
p1.display('Ali', 'ME')


# # Exception Handling

# In[36]:


print(7/0) #Zero division exception


# In[37]:


print(a) #name error exception


# In[38]:


a=[2,3] #out of bound index exception
a[7]


# In[39]:


dic1 = {'a':20, 'b':25} #key error exception
dic1['z']


# In[40]:


open("abc.txt") #file not found error


# In[41]:


int('7.2') #value error


# In[42]:


int('a') #value error


# In[43]:


list(2032) #Type error


# In[44]:


list('2032')


# In[45]:


try:
    print(6/0)
except ZeroDivisionError:
    print("OHO")


# In[54]:


print("start.....")
      
try:
      open('a.txt')
except FileNotFoundError:
    print("OHH NO")


# In[55]:


print("start.....")
      
try:
      open('a.txt')
except FileNotFoundError:
    print("OHH NO File")
try:
    a=[2,3]
    print(a[7])
    
except IndexError:
    print("OHH Out of Boundd")
try:
      print(0/0)
except ZeroDivisionError:
    print("OHH 0/O")


# # Raise

# In[67]:


class Student():
    def __init__(self,age):
        self.age=age
        if age in range(18,81):
            raise Exception ("age range 18 to 88")
        
obj1= Student(19)
obj1.age


# In[70]:


class Student():
    def __init__(self,age):
        self.age=age
        if (age< 18 or age> 80):
            raise Exception ("age range 18 to 88")
        
obj1= Student(10)
obj1.age


# In[ ]:




