#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import ast
token=[]
operator=['+','-','*','/','<','>']
datatype=['int','char', 'float']
punctuator=['[',']','{','}','(',')',',']
special_char=['#','$','%','&']

expression= "int = [ ( a + b & & 2 + 4 ) ]"
exp=re.split('\s', expression)
print("splited expression:" , (exp))
for word in exp:
    if word in ['str','int','char']:
        token.append(['Datatype',word])
    elif re.match("[a-z]",word) or re.match("[A-Z]",word):
        token.append(['identifier',word])
    elif word in operator:
        token.append(['operator',word])
    elif word in datatype:
        token.append(['datatype',word])
    elif word in punctuator:
        token.append(['punctuator',word])
    elif word in special_char:
        token.append(['special_character',word])
    elif re.match("[0-9]",word):
        token.append(['integer',word])
print("  ")      
print(token)
print(" ")
print("Parse tree")
parse_expression="( 3 + ( 4 + 5 ) ) "
code = ast.parse(parse_expression, mode='eval')  
print("calculated answer:", eval(compile(code, '', mode='eval')))
print("  ")       

print(ast.dump(code)) 


# In[ ]:




