import math

list_of_numbers = input()

num1, num2, num3, num4, num5 = list_of_numbers.split()
num1, num2, num3 = float(num1), float(num2), float(num3)
num4, num5 = float(num4), float(num5)

mean = (num1 + num2 + num3 + num4 + num5) / 5

std = math.sqrt((math.pow(num1-mean,2)+math.pow(num2-mean, 2)+math.pow(num3-mean, 2)+math.pow(num4-mean, 2)+math.pow(num5-mean, 2))/5)

std = round(std, 3)

print(std)