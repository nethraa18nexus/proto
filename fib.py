def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return[0,1]
    else:
        series=[0,1]
        for i in range(2,n):
            next_term=series[i-1]+series[i-2]
            series.append(next_term)
        return series
terms=int(input("Enter terms: "))
result=fibonacci(terms)
print(f"fibonacci series ({terms} terms): {result}")