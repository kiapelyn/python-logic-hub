num_calls = 0

def fib(x: int) -> int:
    global num_calls
    if x == 0: return 0
    elif x == 1: return 1
    num_calls += 2
    return fib(x-1) + fib(x-2)
    
y = int(input())
for i in range(y):
    x = int(input())
    num_calls = 0
    fibo = fib(x)
    print(f"fib({x}) = {num_calls} calls = {fib(x)}")