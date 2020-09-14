#!/usr/bin/env python
# coding: utf-8

# # First Program

# In[8]:


p = int(input("\n Enter the principal amount:"))
t = int(input("\n Enter the time period:"))
r = int(input("\n Enter the rate of interest:"))
sample = p*t*r/100
print("\n Simple Interest:",sample)


# # Output using Print

# In[11]:


print('''This sentence is output to the screen''')
a=5
print("The value of a is:",a)
print('x:',1,2,3,4)
x = 5 ; y = 10
print('The value of x is {} and y is {}'.format(x,y))
print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))


# In[10]:


print('Hello, {greeting}'.format(greeting = 'Good morning!',))


# In[12]:


x = 12.3456789
print('The value of x is %3.2f' %x)
print('The value of x is %3.4f' %x)


# In[13]:


for x in range(1, 11):
     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


# In[14]:


table = {'abc': 123456789, 'efg': 234567891, 'hij': 345678901}
for name, phone in table.items():
     print('{0:10} ==> {1:10d}'.format(name, phone))


# In[15]:


import math
print('the value of pi approximately is %5.3f.' % math.pi)


# # Input Using input

# In[16]:


x = input('Enter a string:')
print("The entered string is:{0}".format(x))
y = int(input('Enter a integer:'))
print("The entered integer is:",y)
z = float(input('Enter a floating point number:'))
print("The entered real number is:",z)


# # Multiline Statements

# In[17]:


x = ('1' + '2' +
     '3' + '4')
y = '1' + '2' + '11' + '12'
weekdays = ['Monday', 'Tuesday', 'Wednesday','Thursday', 'Friday']
weekday = {'one':'Monday'}
print ('x has a value of', x)
print ('y has a value of', y)
print(weekdays)
print(weekday)


# In[18]:


import os
x = 'hello'
print(x)


# 
# # Conditional Execution

# # Example code for 'if' statement

# In[19]:


var = -1
if var < 0:
    print(var)
    print("the value of var is negative")
if ( var == -1 ) : 
    print("the value of var is negative")


# In[20]:


var = 1
if var < 0:
    print("the value of var is negative")
    print(var)
else:
    print("the value of var is positive")
    print(var)


# In[21]:


score = 95
if score >= 99:
    print('A')
elif score >= 75:    
    print('B')
elif score >= 60:    
    print('C')
elif score >= 35:    
    print('D')
else:    
    print('F')


# # Iteration

# ## Use of for loop

# In[22]:


print("first example")
for item in [1,2,3,4,5]:
    print('item :', item)
print("Second Example")
letters = ['A', 'B', 'C']
for index in range(len(letters)):
    print('First loop letter :', letters[index])


# In[23]:


count = 0
while (count <3):
    print('The count is:', count)
    count = count + 1


# # Lists

# In[24]:


list_1 = ['Statistics', 'Programming', 2016, 2017, 2018]
list_2 = ['a', 'b', 1, 2, 3, 4, 5, 6, 7 ]
print("list_1[0]: ", list_1[0])
print("list2_[1:5]: ", list_2[1:5])


# In[25]:


print("list_1 values: ", list_1)
list_1.append(2019)
print("list_1 values post append: ", list_1)


# In[26]:


print("Values of list_1: ", list_1)
print("Index 2 value : ", list_1[2])
list_1[2] = 2015;
print("Index 2's new value : ", list_1[2])


# In[27]:


print("list_1 values: ", list_1)
del list_1[2];
print("After deleting value at index 2 : ",list_1)


# # Example code for basic operation on lists

# In[28]:


import string
import operator
print("Length: ", len(list_1))
print("Concatenation: ", [1,2,3] + [4, 5, 6])
print("Repetition :", ['Hello'] * 4)
print("Membership :", 3 in [1,2,3])
print("Iteration :")
for x in [1,2,3]: print(x)
print("slicing :", list_1[-2])
print("slicing range: ", list_1[1:])
print("Max of list: ", max([1,2,3,4,5]))
print("Min of list: ", min([1,2,3,4,5]))
print("Count number of 1 in list: ", [1,1,2,3,4,5,].count(1))
list_1.extend(list_2)
print("Extended :", list_1)
print("Index for Programming:",list_1.index('Programming'))
print (list_1)
print("pop last item in list: ", list_1.pop())
print("pop the item with index 2: ", list_1.pop(2))
list_1.remove('b')
print("removed b from list: ", list_1)
list_1.reverse()
print("Reverse: ", list_1)
list_1 = ['a','c','b']
list_1.sort()
print("Sort ascending: ", list_1)
list_1.sort(reverse = True)
print("Sort descending: ", list_1)


# # Tuples

# In[29]:


Tuple = ()
print("Empty Tuple: ", Tuple)
Tuple = (1,)
print("Tuple with single item: ", Tuple)
Tuple = ('a','b','c','d',1,2,3)
print("Sample Tuple :", Tuple)


# In[30]:


Tuple = ('a', 'b', 'c', 'd', 1, 2, 3)
print("3rd item of Tuple:", Tuple[2])
print("First 3 items of Tuple", Tuple[0:2])


# In[31]:


Tuple = ('a','b','c','d',1,2,3)
print("Length of Tuple: ", len(Tuple))
Tuple_Concat = Tuple + (7,8,9)
print("Concatinated Tuple: ", Tuple_Concat)
print("Repetition: ", (1,'a',2, 'b') * 3)
print("Membership check: ", 3 in (1,2,3))
for x in (1, 2, 3): print(x)
print("Negative sign will retrieve item from right: ", Tuple_Concat[-2])
print("Sliced Tuple [2:] ", Tuple_Concat[2:])
print("Max of the Tuple (1,2,3,4,5,6,7,8,9,10): ",
max((1,2,3,4,5,6,7,8,9,10)))
print("Min of the Tuple (1,2,3,4,5,6,7,8,9,10): ",
min((1,2,3,4,5,6,7,8,9,10)))
print("List [1,2,3,4] converted to tuple: ", type(tuple([1,2,3,4])))


# # Dictionary

# In[32]:


dict = {'Name': 'asd', 'Age': 15, 'Class': 'Tenth'}
print("Sample dictionary: ", dict)


# In[33]:


print("Value of key Name, from sample dictionary:", dict['Name'])


# In[34]:


dict0 = {'Name': 'xyz', 'Age': 20, 'Class': 'BE'}
print("Sample dictionary: ", dict0)
k=1
for i in dict0:
    print(k,i,dict0[i])
    k=k+1
del (dict0['Name'])
print("Sample dictionary post deletion of item Name:", dict0)
dict0 = {'Name': 'xyz', 'Age': 20, 'Class': 'BE'}
dict0.clear() 
print("dict post dict.clear():", dict0)
dict = {'Name': 'xyz', 'Age': 20, 'Class': 'BE'}
del (dict0)


# In[35]:


dict = {'Name': 'asd', 'Age': 20, 'Class': ' BE'}
print("Sample dictionary: ", dict)
dict['Age'] = 20.6
print("Dictionary post age value update: ", dict)


# In[36]:


dict = {'Name': 'as', 'Age': 20, 'Class': ' BE'}
print("Length of dict: ", len(dict))
dict1 = dict.copy()
print("Copy:\n",dict1)
print("Value for Age: ", dict.get('Age'))
print("dict items: ", dict.items())
print("dict keys: ", dict.keys())
print("Value of dict: ", dict.values())
dict1 = {'Name': 'asd', 'Age': 20}
dict2 = {'Sex': 'm' }
dict1.update(dict2)
print("dict1.update(dict2) = ", dict1)


# # User-defined Functions

# In[37]:


def helloFunction():
    print("Hello World")
helloFunction()


# In[38]:


def sum_numbers(x, y):
        return x + y
print(sum_numbers(1,2))


# In[39]:


def sample_function(*args):
    for a in args:
        print(a)
sample_function(1,2,3)


# In[41]:


def sample_function(**args):
    for a in args:
        print(a, args[a])
sample_function(name='abcd', age=20)


# In[42]:


print("list_1 values: ", list_1)
list_1.append(2020)
print("list_1 values post append: ", list_1)


# In[45]:


x = 10

def sum_two_numbers(y):
    return x + y

print(sum_two_numbers(20))


# In[44]:


def add(x, y): 
    return x + y
print("FUNCTION ADD:\n",add(2,2))
add = lambda x, y : x + y 
print("LAMBDA ADD :\n",add(2,2))


# In[ ]:




