num=int(input("enter a number: "))
limit=int(input("enter limit: "))
print(f"\n multiplication table of {num} upto {limit} :")
print("*"*35)
for i in range(1,limit+1):
    product = num*i
    print(f"{num:3} x {i:3} = {product:4}")