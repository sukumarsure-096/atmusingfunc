class overloading():
    def parameters(self,a= None,b=None,c=None,d=None):
        if a!= None and b!=None and c!=None and d!=None:
            totalmarks = a+b+c+d
            print('totalmarks : ',totalmarks)
            avg = totalmarks/4
            print('avg of marks :',avg)
            per = (totalmarks/400)*100
            print(per)
            if per>75 :
                print('first class')
            elif per >65 and per<75:
                print('second class')
            elif per>55 and per<65:
                print('third class')
            else:
                print('just pass')
        elif a!= None and b!=None and c!=None:
            if a>b and a>c:
                print('a is greater')
            elif b>c:
                print('b is greater')
            else :
                print('c is greater')
        elif a!= None and b!=None:
            for num in range(a,b+1):
              for i in range(2,num):  
                if(num%i==0):
                 break 
              else:print(num)
        elif a!= None:
            temp=a
            res=0
            while temp:
                fact=1
                i=1
                rem=temp%10
                while i<=rem:
                    fact = fact*i
                    i=i+1
                res = res+fact
                temp = temp//10
            if res==a:
                print('strong')
            else:
                print('not strong')
        else:
            num = int(input('enter a number : '))
            temp = num
            len = 0
            while temp:
                #n = temp%10
                len = len+1
                temp = temp//10
            #print(len)
            temp = num
            res=0
            while temp:
                d=temp%10
                res = res+d**(len)
                temp=temp//10
            if res == num:
                print('arm strong')
            else:
                print('not arm strong')

 
s = overloading()
s.parameters()
