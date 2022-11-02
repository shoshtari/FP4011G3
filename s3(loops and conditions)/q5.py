def is_prime(x):
    if x==1:
        return False
    i = 2
    while i*i <= x:
        if x%i==0:
            return False
        i += 1
    return True

a, b = map(int, input().split())
for i in range(a, b):
    if is_prime(i):
        print(i)

