import math

def size(x):
    return int(math.log10(x)) + 1

def is_armstrang(x):
    ans = 0
    n = size(x)
    X = x
    while x!=0:
        o = x%10
        x = x//10
        ans += o**n
    return ans==X


