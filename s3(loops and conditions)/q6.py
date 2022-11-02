def is_prime(x):
    if x==1:
        return False
    i = 2
    while i*i <= x:
        if x%i==0:
            return False
        i += 1
    return True

def soloution1(x):
    for i in range(2, x):
        if x%i==0 and is_prime(i):
            print(i)


def soloution2(x):
    # it is output is same with soloution1 just it use another approach

    i = 2
    while x!=1:
        if x%i==0:
            print(i)
            while x%i==0:
                x = x//i
        i += 1

n = int(input())

soloution2(n)
