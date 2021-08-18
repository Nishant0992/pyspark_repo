# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:40:43 2021

@author: Nishant
"""

#List remove append

input_list=['SAS', 'R', 'PYTHON', 'SPSS']
input_list[3]='SPARK'
print(input_list)

#String to list conversion

input_str='I love Data Science & Python'
mod_input=input_str.strip(' ')
output_list=mod_input.split()
print(output_list)

#List to string conversion

input_list=['Python syntax is easy to learn','Python syntax is very clear']
output_str=' & '.join(input_list)
print(output_str)

#Nested List
input_list = [['SAS','R'],['Tableau','SQL'],['Python','Java']]
print(input_list[2][0])

#It’s the time to disco

t = ("disco", 12, 4.5)
print(t[0][2])

#String palindrome

input_str='New'
rev_str=input_str[::-1]
if input_str.lower()==rev_str.lower():
    print(1)
else:
    print(0)
    
#Reverse words
input_str='A string, which will consist of a few spaces.'
new_list=input_str.split()
new_list.reverse()
output_str=' '.join(new_list)
print(output_str)

#String Formatting
input_str='caloRie ConsuMed'
mod_str=input_str.lower()[:7] +'_'+ input_str.lower()[8:]
print(mod_str)

input_str='data science'
mod_str=input_str[:4]+'_'+input_str[5:]
print(mod_str)

#Multiple choice questions
#1
s='I love Python'
print(s[2:6])
print(s[-11:-7])

#2
print(3 * 3 ** 3)

#3
print( ((500//7) % 5) ** 3)

#4
#T = (3, 5, 7, 11)
#T.append(9)
#print(T)

#6
l = [32, 34, 12, 27, 33]
l.append((14, 19))
print(len(l))

#10
print(list(range(10, 1, -1)))





