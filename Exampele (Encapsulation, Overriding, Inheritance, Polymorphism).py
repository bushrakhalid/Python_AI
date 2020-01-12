#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Inheritance
class Animal: #parent class

    def __init__(self): 
        print("Animal created")

    def whoI(self):
        print("Animal")

class Dog(Animal): #Child class inherited from Animal -> parent

    def __init__(self):
        super().__init__()
        
        print("Dog created")

    def whoAmI(self):
        print("Dog")


d = Dog()
d.whoAmI()
d.whoI()


# In[7]:


#polymorphism

class Animal:
    def __init__(self, name=''): 
        self.name = name
        
    def talk(self):
        pass

class Cat(Animal):
     def talk(self):
            print("Meow!")

class Dog(Animal):
    def talk(self):
        print("Woof!")


a = Animal()
a.talk()

c = Cat()
c.talk()

d = Dog()
d.talk()


# In[8]:


#Overriding

class Robot:
    def action(self):
        print('Robot action')

class HelloRobot(Robot):
    def action(self):
        print('Hello world')

r = HelloRobot()
r.action()


# In[9]:


#Abstract Class

from abc import ABC, abstractmethod 
class Animal(ABC): 
  
    def move(self): 
        pass
  
class Human(Animal): 
  
    def move(self): 
        print("I can walk and run") 
  
class Snake(Animal): 
  
    def move(self): 
        print("I can crawl") 
  
        
R = Human() 
R.move() 

K = Snake() 
K.move() 


# In[ ]:




