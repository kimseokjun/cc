import fibo

while True:
    i = int(input("몇 번째 항 : "))
    val, count= fibo.fibonacci(i-1)
    print(val)
    print('count=', count)
