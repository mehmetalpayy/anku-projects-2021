stack = []
appendnum= eval(input('How many items do you want to add(int): '))
for i in range(appendnum):
    add= str(input('Which one letter or word: '))
    stack.append(add)
    print(stack)

pop_num= eval(input('How many items do you want to remove from last added(int): ')) 
print('list before pop method',stack)
if appendnum>=pop_num:
    for i in range(pop_num):
            #peek and pop code
            peek=stack[-1]
            stack.pop()
            print('removed element is {0} and list {1} after {2} pop method '.format(peek,stack,i+1))
#check is_empty()
print('True for list is empty and False for list is nonempty >>>>>>', end=' ') 
if len(stack)==0:
    print(stack==[])
else:
    print(stack==[])
