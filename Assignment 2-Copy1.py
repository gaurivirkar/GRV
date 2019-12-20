#!/usr/bin/env python
# coding: utf-8

# # Implement List comprehensions to produce the following lists.
# Write List comprehensions to produce the following Lists
# 
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]]
# 
# [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# 
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
# 

# In[14]:


lst1= [x for x in "acadglid"]
lst1


# In[16]:


input_list=["x","y","z"]
lst2=[i*num for i in input_list for num in range(1,5)]
lst2


# In[23]:


input_list=["x","y","z"]
lst3=[i*num  for num in range(1,5) for i in input_list]
lst3


# In[34]:


input_list1=[2,3,4]
lst4=[[i+num]  for i in input_list1 for num in range(0,3)]
lst4


# In[32]:


input_list1=[2,3,4,5]
lst5=[[i+num  for i in input_list1] for num in range(0,4)]
lst5


# In[35]:


input_list=[1,2,3]
l6 = [ (j,i) for i in input_list for j in input_list]
l6


# # Implement a function longestWord() that takes a list of words and returns the longest one.

# In[75]:


word_length=[]
def longestWord(word_list):
    for i in word_list:
        word_length.append((len(i),i))
    word_length.sort()
    return word_length[-1][1]
     


# In[76]:


print(longestWord(["Hi","Homesick", "Hello"]))


# # Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.

# In[2]:



def filter_long_words(list1):
    words1=[]
    n=int(input("Enter an integer:"))
    for i in list1:
        if(len(i)>n):
            words1.append(i)
    return(words1)


print(filter_long_words(["Hi", "Hello","Home", "Few","Many"]))


# # Write a Python program using function concept that maps list of words into a list of integers representing the lengths of the corresponding words.
# Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
# Here 2,3 and 4 are the lengths of the words in the list.

# In[3]:


list1=[]
def mapping(wlist):
    for i in wlist:
        list1.append(len(i))
    return(list1)


print(mapping(["Hi", "Hello","Home", "Few","Many"]))        
    


# # Write a Python function which takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.
# 

# In[15]:


def check_vowel(char_list):
    for i in char_list:
        if(i=='a'or i=='e' or i=='i' or i=='u'or i=='o'):
            return True
        else:
            return False
            
char_list=['a','c','f','g','o']
           
list(map(check_vowel,char_list))


# In[ ]:




