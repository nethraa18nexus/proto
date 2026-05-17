setA={1,2,3,4,5}
setB={4,5,6,7,8}
union_result=setA.union(setB)
intersection_result=setA.intersection(setB)
print(union_result)
print(intersection_result)
difference_result=setA.difference(setB)
print(difference_result)
setx={1,2}
sety={1,2,3,4,5}
print("is x subset of y?:",setx.issubset(sety))
print("is y subset of x?:",sety.issubset(setx))
print("is x superset of y?:",setx.issuperset(sety))
print("is y superset of x?:",sety.issuperset(setx))