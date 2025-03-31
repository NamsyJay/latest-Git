# Iterative Method.
def fibonaci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a + b
    return a

print (fibonaci(10))

# Recursive Method.
def fibonaci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonaci_recursive(n-1) + fibonaci_recursive(n-2)
    
print (fibonaci_recursive(10)) 