#Python Program for n-th Fibonacci number

n=int(input("Enter the limit: "))

def fibonacci(n):
    if n<=0:
        print("Incorrect Input")
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

fibo=fibonacci(n)
print(fibo)