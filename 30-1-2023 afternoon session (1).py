#!/usr/bin/env python
# coding: utf-8

# In[8]:


#rock paper scissor
from random import randint
n=int(input("enter a number of turns:"))
choice=["rock","paper","scissor"]
sum=0
count=0
for i in range(n):
    user=input(f"choose from {choice}")
    computer=choice[randint(0,2)]
    print(computer)
if user==computer:
    print("DRAW MATCH")
    sum=sum+1
elif user== "paper" and computer=="rock":
    print("user 1 wins")
    sum=sum+1
elif user== "rock" and computer=="scissor":
    print("user 1 wins")
    sum=sum+1
elif user== "scissor" and computer=="paper":
    print("user 1 wins")
    sum=sum+1
else:
    print("computer 1 wins")
    cout+=1
print("user score:",sum)
print("computer score:",count)
if sum>count:
    print("user 1 wins")
else:
   print("computer wins")


# In[ ]:





# In[ ]:




