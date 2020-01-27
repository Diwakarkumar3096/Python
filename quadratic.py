#import complex math module
import cmath

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))

#calculate the discrimininant

d=(b**2)-(4*a*c)

#find two solution
sol1=(-b -cmath.sqrt(d)/(2*a))
sol2=(-b +cmath.sqrt(d)/(2*a))

print("the solution are {0} and {1}".format(sol1,sol2))



