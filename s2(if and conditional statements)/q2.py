year, month, day = map(int, input().split('/'))

# Leap year
is_leap = (year%33)%4==1
if day > 31 or (day == 31 and month > 6) or (day == 30 and not is_leap):
    print("day number is not valid!")
    exit(0)
if not 1 <= month <= 12:
    print("month number is not valid!")
    exit(0)
if is_leap:
    print("leap year")
else:
    print("not leap year")


# month data

if month == 1:
    print("farvardin")
Ü    print("31")
if month == 2:
    print("ordibehesht")
    print("31")
if month == 3:
    print("khordad")
    print("31")
if month == 4:
    print("tir")
    print("31")
if month == 5:
    print("mordad")
    print("31")
if month == 6:
    print("shahrivar")
    print("31")
if month == 7:
    print("mehr")
    print("30")
if month == 8:
    print("aban")
    print("30")
if month == 9:
    print("azar")
    print("30")
if month == 10:
    print("dey")
    print("30")
if month == 11:
    print("bahman")
    print("30")
if month == 12:
    print("esfand")
    if is_leap:
        print("30")
    else:
        print("29")
number_of_weeks = ((day - 1)//7) + 1
print(number_of_weeks)

