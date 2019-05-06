# The programm will summ all numbers, which you will input. To break type 0. Creator: nacmop (06.05.2019)

b = 0
a = None
while a != 0:
    a = int(input())
    if a != 0:

        b += a
    else:
        print(b)