import math

a = int(input())

r = a%10

n = math.log10(a)
n = int(n) # n = math.trunc(n)

l = a//(math.pow(10, n))

remain = a - r - l*math.pow(10, n)

print(int(remain + l + r*(math.pow(10, n))))