def sum_list(numbers):
    total=0
    for num in numbers:
        total+=num
    return total
numbers=[1,2,3,4,5]
print("list:",numbers)
print("sum:",sum_list(numbers))