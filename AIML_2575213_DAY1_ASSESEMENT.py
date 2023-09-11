#!/usr/bin/env python
# coding: utf-8

# # 1.Manipulate using a list.
# i)To add new elements to the end of the list
# ii)To reverse elements in the list
# iii)To display the same list of elements multiple times.
# iv)To concatenate two list
# v)To sort the elements in the list in ascending order.

# In[45]:


#i)To add new elements to the end of the list
list1=['java','python','sql']
list1


# In[53]:


list1.append('aws')
list1


# In[55]:


list1.pop()
list1.pop()
list1.pop()
list1


# In[8]:


#ii)To reverse elements in the list
list1.reverse()
list1


# In[57]:


#iii)To display the same list of elements multiple times.
list1*3


# In[58]:


list2=['abc','def']
list2


# In[60]:


#iv)To concatenate two list
l=list1+list2
l


# In[61]:


#v)To sort the elements in the list in ascending order.
l.sort()
l


# # 2.Write a Python program to do in the tuples.
# i)Manipulate using tuples.
# ii)To add new elements to the end of the tuples
# iii)To reverse elements in the list
# iv)To display the elements of the same tuple multiple times.
# v)To concatenate two tuples
# vi)To sort the elements in the list in ascending order.

# In[5]:


#i)Manipulate using tuples.
tuple1=(22,34,78)
tuple1=list(tuple1)
print(tuple1)
print(type(tuple1))


# In[115]:


#ii)To add new elements to the end of the tuples
tup=(1,2,3)
tuple1=tup+(6,7)
print(tuple1)


# In[119]:


#iii)To reverse elements in the list
tuple1=(1,3,5,7)
tuple1=tuple1[: :-1]
tuple1


# In[120]:


#iv)To display the elements of the same tuple multiple times.
tuple1*3


# In[2]:


#v)To concatenate two tuples
t1=(1,2,3)
t2=(9,8,7)
t=t1+t2
print(t)


# In[12]:


#vi)To sort the elements in the list in ascending order.
tuple1=(22,34,7)
tuple1=list(tuple1)
tuple1.sort()
print(tuple1)


# # 3.Write a python program to implement the following using list.
# i)Create a list with integers(minimum 10 numbers)
# ii)How to display the last number in the list.
# iii)Command for displaying the values from the list[0:4]
# iv)Command for displaying the values from the list[2:]
# v)Command for displaying the values from the list[:6]

# In[13]:


#i)Create a list with integers(minimum 10 numbers)
lst=[76,27,18,29,56,9,11,7,10,84]
lst


# In[21]:


#ii)How to display the last number in the list.
lst=[76,27,18,29,56,9,11,7,10,84]
last_num=lst[len(lst)-1]
last_num


# In[24]:


#iii)Command for displaying the values from the list[0:4]
lst=[76,27,18,29,56,9,11,7,10,84]
lst=lst[0:4]
print(lst)


# In[25]:


#Command for displaying the values from the list[2:] 
lst=[76,27,18,29,56,9,11,7,10,84]
lst=lst[2:]
lst


# In[26]:


# v)Command for displaying the values from the list[:6]
lst=[76,27,18,29,56,9,11,7,10,84]
lst=lst[:6]
lst


# # 4.Write a Python program:tuple1=(10,50,20,40,30)
# i)To display the elements 10 and 50 from tuple1.
# ii)To display the length of a tuple1.
# iii)To find the minimum element from tuple1.
# iv)To add all the elements in the tuple1.
# v)To display the same tuple1 multiple times.

# In[30]:


#i)To display the elements 10 and 50 from tuple1.
tuple1=(10,50,20,40,30)
tuple1[0:2]


# In[31]:


# ii)To display the length of a tuple1.
len(tuple1)


# In[34]:


# iii)To find the minimum element from tuple1.
tuple1=(10,50,20,40,30)
min(tuple1)


# In[41]:


#iv)To add all the elements in the tuple1.
tuple1=(10,50,20,40,30)
lst=list(tuple1)
lst1=lst[0]+lst[1]+lst[2]+lst[3]+lst[4]
print(lst1)


# In[42]:


tuple1=(10,50,20,40,30)
sum(tuple1)


# In[43]:


#v)To display the same tuple1 multiple times.
tuple1=(10,50,20,40,30)
tuple1*3


# # 5.Write a Python program:
# i)To calculate the length of the string
# ii)To reverse words in a string
# iii)To display the same string multiple times
# iv)To concatenate two strings
# v)Str1="South India",using string slicing to display "India"

# In[44]:


#i)To calculate the length of the string
Str="sirisha"
len(Str)


# In[62]:


#ii)To reverse words in a string
Str="sirisha"
l=len(Str)
print(Str[::-1])


# In[64]:


#iii)To display the same string multiple times
Str*4


# In[66]:


#iv)To concatenate two strings
Str='sirisha'
Str1='kandula'
Str+' '+Str1


# In[67]:


#v)Str1="South India",using string slicing to display "India"
Str1="South India"
Str1[6:]


# # 6.Perform the following:
# i)Creating the Dictionary.
# ii)Accessing values and keys in the Dictionary.
# iii)Updating the dictionary using the function.
# iv)Clear and delete the ductionary values.

# In[68]:


#i)Creating the Dictionary.
dict={'key1':'book','key2':'pen','key3':'table'}
dict


# In[84]:


#ii)Accessing values and keys in the Dictionary.
dict={'key1':'book','key2':'pen','key3':'table'}
d=dict.get('key2')
print(d)
access_key=dict.keys()
print(access_key)
access_value=dict.values()
print(access_value)


# In[ ]:


#iii)Updating the dictionary using the function.


# In[93]:


#iv)Clear and delete the ductionary values.
dict={'key1':'book','key2':'pen','key3':'table'}
d=dict.pop("key3")
print(d)
c=dict.clear()
print(c)


# # 7.Python program to insert a number to any position in a list.

# In[110]:


lst=['siri',876,'@*']
lst.insert(2,27)
print(lst)


# # 8.Python program to delete an element from a list by index.

# In[116]:


lst=['siri',876,'@*']
del lst[2]
lst


# # 9.Write a program to display a number from 1 to 100.

# In[194]:


for i in range(1,101):
  print(i,end=" ")
#for i in range(1,101):
#    if(i<=100):
#       print(i)
#    else:
 #     break


# # 10.Write a Python program to find the sum of all items in a tuple.

# In[146]:


tuple1=(2,4,7,0)
sum(tuple1)


# # 12.A list of words is given.Find the words from the list that have their second character in uppercase.
# ls=['hello','Dear','hOw','ARe','You']

# In[170]:


ls=['hello','Dear','hOw','ARe','You']
ls1=[]
for i in ls:
    if(i[1].isupper()):
        ls1.append(i)
print(ls1)


# # Control Structures:   

# In[209]:


# 1.Write a python program to find the first N Prime numbers.


# In[ ]:





# In[ ]:




