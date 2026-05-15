def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def lcm(a,b):
    return (a*b)//gcd(a,b)
num1=int(input("enter first number"))
num2=int(input("enter second number"))
gcd_result=gcd(num1,num2)
lcm_result=lcm(num1,num2)

print(f"GCD OF {num1} and {num2} is {gcd_result}")
print(f"LCM of {num1} and {num2} is {lcm_result}")