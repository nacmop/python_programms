age1 = input("Введите Ваш возраст: ")
# age = int(age1)
last_symbol_of_age = int(age1[-1])
first_symbol_of_age = int(age1[-2])
if 2<=last_symbol_of_age<=4 & first_symbol_of_age != 1:
    print("Вам " + age1 + " года")

if last_symbol_of_age == 1:
    print("Вам " + age1 + " год")
else :
    print("Вам " + age1 + " лет")
