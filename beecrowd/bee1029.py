def fib(x: int) -> int:
    global num_calls
    num_calls += 1
    if x == 0: return 0
    elif x == 1: return 1
    return fib(x-1) + fib(x-2)
    
def main():
    x = int(input())
    fibo = fib(x)
    print(f"fib({x}) = {num_calls} calls = {fib(x)}")
    
y = int(input())
for i in range(y):
    if __name__=="__main__":
        num_calls = -1
        main()