a = int(input())
b = int(input())
c = int(input())

s = a + b + c

a, c = min(a, b, c), max(a, b, c)
b = s - a - c

if a*a + b*b == c*c:
    print("YES")
else:
    print("NO")
