#!/usr/bin/env python
# coding: utf-8

# In[5]:


class Student:
    name = "Random Name"
    roll_number = 100
    
obj = Student()
print(obj.name)
print(obj.roll_number)


# In[6]:


#get set value
class Student:
    name = "Yashwanthni"
    __rollnumber = "100" #private variable
    
    def get_rollnumber(self):
        return self.__rollnumber
    def set_rollnumber(self):
            self.__rollnumber
obj = Student()
print(obj.name)
print(obj.get_rollnumber())


# In[17]:


n = int(input())
arr=[]
for i in range(n):
    username=input("enter username:")
    pswd=input("enter pswd:")
    arr.append({username: pswd})
print(arr)


# In[21]:


n = int(input())
arr=[]
for i in range(n):
    username=input("enter username:")
    pswd=input("enter pswd:")
    arr.append({username: pswd})
print(arr)
username1=input("username")
pswd1=input("pswd")
if (username==username1 and pswd==pswd1):
    print("already exists")
else:
    print("does not exist")


# In[26]:


stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
stack.pop(1)
print(stack)


# In[31]:


queue = []
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.pop()
print(queue)


# In[ ]:




