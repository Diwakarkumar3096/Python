Lower=int(input("enter the lower range"))
Upper=int(input("enter the Upper range"))

for num in range(Lower,Upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
          print(num)

