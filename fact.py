num=int(input("enter the number"))
factorial=1

if num<1:
    print("No factorial is exist")
elif num==0:
    print("factorial of 0 is 1")
elif num >1:
    for i in range(1,num+1):
       factorial=factorial*i
       break
     print(factorial,"is the factorial of num")
 
