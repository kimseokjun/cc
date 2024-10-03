
n = int(input("작은 정수를 입력하세요 : "))
m = int(input("큰 정수를 입력하시오 : "))

ans = 1

for i in range(n,m+1):
    ans = ans* i

print("{}에서 {}까지 1씩 증가시켜 가며 모두 곱한 값은 {} 이다".format(n,m,ans))
