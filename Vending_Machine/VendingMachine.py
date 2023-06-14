#!/usr/bin/env python
# coding: utf-8

# In[46]:



def VendingMachineProcess():
    announcement='''You can add a money and buy something constantly
------------------------------------------------------------------    
Click   1            2           3         4             5
      Redbull      IceTea    Lemonade   CocaCola    Orange Juice
------------------------------------------------------------------      
      '''
    print(announcement)
    beverages= ['Redbull','IceTea','Lemonade','CocaCola','Orange Juice']
    stock=[5,5,5,5,5]
    price= [7.5,5,4,6,3.5]
    account= 0
    while True:
        process= eval(input('Click (0) to quit, Click (1) to buy something, Click (2) to add money: '))
        if process==1:
            while True:
                demand = eval(input('Which one do you want to take(0 for quit): '))
                if demand < 6:
                    if demand == 0:
                        print('Get back your money', account)
                        break
                    elif demand == 1:
                        if stock[0]>0 and account>=price[0]:
                            print('You got {0}'.format(beverages[0]))
                            stock[0] -= 1
                            account -= price[0]
                            print('Your current money is', account)

                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[0]))
                            print('Your current money is', account)

                    elif demand == 2:
                        if stock[1]>0 and account>=price[1]:
                            print('You got {0}'.format(beverages[1]))
                            stock[1] -= 1
                            account -= price[1]
                            print('Your current money is', account)
                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[1]))
                            print('Your current money is', account)

                    elif demand == 3:
                        if stock[2]>0 and account>=price[2]:
                            print('You got {0}'.format(beverages[2]))
                            stock[2] -= 1
                            account -= price[2]
                            print('Your current money is', account)

                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[2]))
                            print('Your current money is', account)
                    elif demand == 4:
                        if stock[3]>0 and account>=price[3]:
                            print('You got {0}'.format(beverages[3]))
                            stock[3] -= 1
                            account -= price[3]
                            print('Your current money is', account)
                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[3]))
                            print('Your current money is', account)

                    elif demand == 5:
                        if stock[4]>0 and account>=price[4]:
                            print('You got {0}'.format(beverages[4]))
                            stock[4] -= 1
                            account -= price[4]
                            print('Your current money is', account)

                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[4]))
                            print('Your current money is', account)

                    else:
                        print('Invalid Input')
                else:
                    print('Invalid Input')   
        elif process==2:
            yourmoney= eval(input('How much money do you want to add: '))
            account += yourmoney
            print('Your current money is ', account)
        elif process== 0:
            print('iyi günler')
            break
            
        else:
            print('Invalid Input')

    
    
    
                     


# In[48]:


VendingMachineProcess()


# In[51]:


def VendingMachineProcess():
    announcement='''You can add a money and buy something constantly
------------------------------------------------------------------    
Click   1            2           3         4             5
      Redbull      IceTea    Lemonade   CocaCola    Orange Juice
------------------------------------------------------------------      
      '''
    print(announcement)
    beverages= ['Redbull','IceTea','Lemonade','CocaCola','Orange Juice']
    stock=[5,5,5,5,5]
    price= [7.5,5,4,6,3.5]
    account= 0
    while True:
        process= eval(input('Click (0) to quit, Click (1) to buy something, Click (2) to add money: '))
        if process==1:
            while True:
                demand = eval(input('Which one do you want to take(0 for quit): '))
                if demand < 6:
                    if demand == 0:
                        print('Get back your money', account)
                        break
                    elif demand >0:
                        if stock[demand-1]>0 and account>=price[demand-1]:
                            print('You got {0}'.format(beverages[demand-1]))
                            stock[demand-1] -= 1
                            account -= price[demand-1]
                            print('Your current money is', account)

                        else:
                            print('Sorry we do not have any {0}, or insufficient money'.format(beverages[demand-1]))
                            print('Your current money is', account)

                    else:
                        print('Invalid Input')
                else:
                    print('Invalid Input')   
        elif process==2:
            yourmoney= eval(input('How much money do you want to add: '))
            account += yourmoney
            print('Your current money is ', account)
        elif process== 0:
            print('Have a good day')
            break
            
        else:
            print('Invalid Input')

VendingMachineProcess()

    
    


# In[ ]:




