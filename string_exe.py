#Exercise 1A: Create a string made of the first, middle and last character

"""string_fml = input("Enter your String: ")
first_str = string_fml[0]
middle_str =  string_fml[len(string_fml)//2]
last_str = string_fml[len(string_fml)-1]
print (first_str +  middle_str + last_str)"""


#Exercise 1B: Create a string made of the middle three characters

"""middle_str = input("Enter your String: ")
mid_value = middle_str[len(middle_str)//2]
before_mid = middle_str[len(middle_str)//2-1]
after_mid = middle_str[len(middle_str)//2+1]
print (before_mid + mid_value + after_mid)"""


#Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.

"""string_1 = input("Enter String S1: ")
string_2 = input("Enter String S2: ")
mid = len(string_1)//2
print (string_1[0:mid] + string_2 + string_1[mid:len(string_1)])"""


#Exercise 3: Create a new string made of the first, middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.


"""string_1 = input("Enter String S1: ")
string_2 = input("Enter String S2: ")
fr = string_1[0] 
fr1 = string_2[0]
mi = string_1[len(string_1)//2]
mi1 = string_2[len(string_2)//2]
la = string_1[len(string_1)-1]
la1 =string_2[len(string_2)-1]
print (fr+fr1+mi+mi1+la+la1)"""


#Exercise 4: Arrange string characters such that lowercase letters should come first
#Given string contains a combination of the lower and upper case letters. 
#Write a program to arrange the characters of a string so that all lowercase letters should come first.


"""from curses.ascii import islower


str_1 = input("Enter a string: ")
low = []
up = []
 
for x in str_1:
  if islower(x):
    low.append(x)
  else:
    up.append(x)
    
low.extend(up)
fnal_str ="".join(low)
print(fnal_str)"""


#Exercise 5: Count all letters, digits, and special symbols from a given string


"""from curses.ascii import isalpha, isdigit
from operator import le
str_1 = input("Enter a string: ")

let =[]
dig =[]
spe =[]

for x in str_1:
  if isalpha(x):
    let.append(x)
  elif isdigit(x):
    dig.append(x)
  else:
    spe.append(x)
print(f"letter in strin: {len(let)}")
print(f"digit in string: {len(dig)}")
print(f"special symbol in string: {len(spe)}")"""


#Exercise 6: Create a mixed String using the following rules
#Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, 
#Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.

"""str1 = input("Enter the string1 :")
str2= input("Enter the string2 :")
avg = ( len(str1)+len(str2))
str2= str2[::-1]
name =""
for i in range(0,avg):
    if i<len(str1):
        name=name+str1[i]
    else:
      pass
    if i<len(str2):
      name=name+str2[i]
    else:
      pass
print(name)"""
#---------------------------------------------------------------------------------------------------------
"""fname = input("Enter Your String: ")
lname = input("Enter Your String: ")
i = 0
j = len(lname)-1
s = ''

while(i < len(fname) or j >= 0):
    if(i < len(fname)):
        s = s + fname[i]
        i += 1
    if(j >= 0):
        s = s + lname[j]
        j -= 1

print(s)"""


# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1
# are present in s2. The character’s position doesn’t matter.


"""from sys import flags


def string_balance_test (s1,s2):
  flag = True
  for char in s1:
    if char in s2:
      continue
    else:
      flag = False
  return flag

s1 = input("Enter a string : ")
s2 = input("Enter a string : ")
flag = string_balance_test(s1,s2)
print ("s1 and s2 are blanced", flag)"""