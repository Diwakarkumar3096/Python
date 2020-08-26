n=int(input("Enter the string to check armstrong:\n"))
t=n;
r=0;
while(n>0):
    a=n%10;
    r=r+a*a*a;
    n=n//10;
if (t==r):
    print("yes it an armstrong:")
else:
    print("No it not armstrong:")
