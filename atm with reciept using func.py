print('\t\t\tSBI ATM \t\t')
account_balance=1000000
pin = (input('enter pin :'))

if len(pin)==4:
    print('select your option')
    print('\t1.account_balance\n \t2.cashwithdraw \n \t3.deposit')
    choice = int(input('enter ur choice :'))
    if choice==1:
            def balance():
                    return account_balance
                
            res = balance()
            print(res)
    elif choice == 2:
            print('enter amount in the multiples 100,500,2000')
            withdraw = int(input('enter withdraw amount;'))
            if withdraw%100==0:
                    if withdraw >=50000:
                            print('daily limit should be less than 50000')
                    else :
                            def cashwithdraw(amount):
                                    return lambda withdraw:account_balance-withdraw
                            #withdraw = int(input('enter withdraw amount;'))
                            res = cashwithdraw(withdraw)
                            #print( res(withdraw))
                            print('do you want reciept \n yes \n no')
                            option = input('select ur option :')
                            if option == 'y':
                                print('\t\t    SBI ATM \t\t')
                                print('\t +++++++++++++++++++++++++++++++\t')
                                print('\t name of holder :    xxxxxxxxxxx ')
                                print('\t account number:    xxxxxxxxxx ')
                                print('\t withdrawal amount :',withdraw)
                                print('\t available balance :',res(withdraw))
                                print('\t +++++++++++++++++++++++++++++++\t')
                                print('\t\t THANK YOU \t\t')
                                
                                
                                #print(res(withdraw))
                            elif option == 'n':
                                print('thank you')
                                
                            
            else:
                    print('please enter amount in the multiples of 100,500,2000')
    elif choice==3:
            print('enter amount in the multiples 100,500,2000')
            deposit = int(input('enter deposit amount:'))
            if deposit%100==0:
                    if deposit >=100000:
                            print('exceed the limit')
                    else:
                            def deposited(amount):
                                    return lambda deposit:account_balance+deposit
                            res = deposited(deposit)
                            #print(res(deposit))
                            print('do you want reciept \n yes \n no')
                            option = input('select ur option :')
                            if option == 'y':
                                print('\t\t        SBI ATM \t\t')
                                print('\t +++++++++++++++++++++++++++++++\t')
                                print('\t name of holder :    xxxxxxxxxxx ')
                                print('\t account number:     xxxxxxxxxx ')
                                print('\t deposit amount :    ',deposit)
                                print('\t available balance :',res(deposit))
                                print('\t +++++++++++++++++++++++++++++++\t')
                                print('\t\t    THANK YOU  \t\t')
                            elif option == 'n':
                                print('thank you,visit again')
                            
                            
            else:
                    print('please valid amount')
else:
    print('please enter valid pin')

            
            
