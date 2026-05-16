def remove_duplicates(original_list):
    unique_list = []

    for item in original_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
numbers = list(map(int,input("enter numbers separated by space: ").split()))
result = remove_duplicates(numbers)
print(f"original numbers: {numbers}")
print(f"list without duplicates: {result}")
print(f"number of elements:original={len(numbers)},after removing duplicates = {len(result)}")