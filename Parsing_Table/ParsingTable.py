#!/usr/bin/env python
# coding: utf-8

# In[59]:


stack = [0]
string = input("Enter your string:\n")
stringlist = []
isaretler = ['*', '-', '/', '+', '(', ')']
for i in range(len(string)):
    if(string[i]== 'i'):
        stringlist.append('id')
    elif(string[i] != 'i' and string[i] != 'd'):
        for isaret in isaretler:
            if(string[i]==isaret):
                stringlist.append(isaret)
stringlist.append('$')
print(stringlist)


# In[60]:


def recursivefunction(x, y):
    #x = stringlist ilk eleman, y = stack son eleman
    if(x == 'id'):
        if(stack[-1]== 0):
            stack.append('id')
            stringlist.pop(0)
            stack.append(5)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==4):
            stack.append('id')
            stringlist.pop(0)
            stack.append(5)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==6):
            stack.append('id')
            stringlist.pop(0)
            stack.append(5)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==7):
            stack.append('id')
            stringlist.pop(0)
            stack.append(5)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])

        else:
            print("INVALID string entered. SYNTAX ERROR!")


    elif(x == '+'):
        if(stack[-1]==1):
            stack.append('+')
            stringlist.pop(0)
            stack.append(6)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==2):
            reduce(stack, 2)
            
        elif(stack[-1]==3):
            reduce(stack, 4)
            
        elif(stack[-1]==5):
            reduce(stack, 6)
            
        elif(stack[-1]==8):
            stack.append('+')
            stringlist.pop(0)
            stack.append(6)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==9):
            reduce(stack[:], 1)
            
        elif(stack[-1]==10):
            reduce(stack, 3)
            
        elif(stack[-1]==11):
            reduce(stack, 5)

        else:
            print("INVALID string entered. SYNTAX ERROR!")


    elif(x == '*'):
        if(stack[-1]==2):
            stack.append('*')
            stringlist.pop(0)
            stack.append(7)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==3):
            reduce(stack, 4)
            
        elif(stack[-1]==5):
            reduce(stack, 6)
            
        elif(stack[-1]==9):
            stack.append('*')
            stringlist.pop(0)
            stack.append(7)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==10):
            reduce(stack, 3)
            
        elif(stack[-1]==11):
            reduce(stack, 5)
            
        else:
            print("INVALID string entered. SYNTAX ERROR!")


    elif(x == '('):
        if(stack[-1]==0):
            stack.append('(')
            stringlist.pop(0)
            stack.append(4)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==4):
            stack.append('(')
            stringlist.pop(0)
            stack.append(4)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==6):
            stack.append('(')
            stringlist.pop(0)
            stack.append(4)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==7):
            stack.append('(')
            stringlist.pop(0)
            stack.append(4)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])

        else:
            print("INVALID string entered. SYNTAX ERROR!")

    
    elif(x == ')'):
        if(stack[-1]==2):
            reduce(stack, 2)
            
        elif(stack[-1]==3):
            reduce(stack, 4)
            
        elif(stack[-1]==5):
            reduce(stack, 6)
            
        elif(stack[-1]==8):
            stack.append(')')
            stringlist.pop(0)
            stack.append(11)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
        elif(stack[-1]==9):
            reduce(stack, 1)
            
        elif(stack[-1]==10):
            reduce(stack, 3)
            
        elif(stack[-1]==11):
            reduce(stack, 5)
            

        else:
            print("INVALID string entered. SYNTAX ERROR!")


    elif(x == '$'):
        if(stack[-1]==1):
            print("VALID string entered. ACCEPTED!")
        elif(stack[-1]==2):
            reduce(stack, 2)
            
        elif(stack[-1]==3):
            reduce(stack, 4)
            
        elif(stack[-1]==5):
            reduce(stack, 6)
            
        elif(stack[-1]==9):
            reduce(stack, 1)
            
        elif(stack[-1]==10):
            reduce(stack, 3)
            
        elif(stack[-1]==11):
            reduce(stack, 5)
        

        
##stacklast = stack[-1] and stacklastsecond = stack[-2]        
def gototable(stacklastsecond,stacklast):
    if (stacklast == 'E'):
        if(stacklastsecond == 0):
            stack.append(1)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        if(stacklastsecond == 4):
            stack.append(8)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
            
    if (stacklast == 'T'):
        if(stacklastsecond == 0):
            stack.append(2)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
            
        if(stacklastsecond == 4):
            stack.append(2)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
            
        if(stacklastsecond == 6):
            stack.append(9)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        
            
    if (stacklast == 'F'):
        if(stacklastsecond == 0):
            stack.append(3)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
            
        if(stacklastsecond == 4):
            stack.append(3)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
            
        if(stacklastsecond == 6):
            stack.append(3)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        if(stacklastsecond == 7):
            stack.append(10)
            print(stack)
            print(stringlist)
            recursivefunction(stringlist[0], stack[-1])
        

             
def reduce(stack, reducenumber):
    rules = ['E + T = E', 'T = E', 'T * F = T', 'F = T', '(E) = F', 'id = F']
    a=0
    b=0
    c=0
    if(reducenumber == 1):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == 'T'):
                a += 1
            if(z == '+'):
                b += 1
            if(z == 'E'):
                c += 1
            if(a==1 and b == 1 and c==1):
                break
        stack.append('E')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])



    if(reducenumber == 2):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == 'T'):
                a += 1
            if(a==1):
                break
        stack.append('E')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])



    if(reducenumber == 3):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == 'T'):
                a += 1
            if(z == '*'):
                b += 1
            if(z == 'F'):
                c += 1
            if(a==1 and b == 1 and c==1):
                break
        stack.append('T')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])



    if(reducenumber == 4):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == 'F'):
                a += 1
            if(a==1):
                break
        stack.append('T')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])


    if(reducenumber == 5):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == ')'):
                a += 1
            if(z == 'E'):
                b += 1
            if(z == '('):
                c += 1
            if(a==1 and b == 1 and c==1):
                break
        stack.append('F')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])


    if(reducenumber == 6):
        while(len(stack)!=0):
            z = stack.pop()
            if(z == 'id'):
                a += 1
            if(a==1):
                break
        stack.append('F')
        print(stack)
        print(stringlist)
        gototable(stack[-2], stack[-1])
                
recursivefunction(stringlist[0], stack[-1])


# In[ ]:




