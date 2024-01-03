print("Hello world")
################### 1 ######################

input: list[str] = input("Введіть три числа через пробіл: ").split()
a, b, c = int(input[0]), int(input[1]), int(input[2])
print("Введіть 1, щоб вивести максимум, 2 - мінімум, 3 - середнє арифметичне: ")

choice = int(input())
if choice == 1:
   print(max(a,b,c))

elif choice == 2:
   print(min(a, b, c))

elif choice == 3:
   print((a + b + c) / 3)

else:
   print("Невірний вибір")

######################### 2 #########################

meters = float(input("Введіть кількість метрів: "))
print("1. Конвертувати в милі\n2. Конвертувати в дюйми\n3. Конвертувати в ярди")
choice = int(input("Ваш вибір: "))
if choice == 1:
   print(meters * 0.000621371192)

elif choice == 2:
   print(meters * 39.3700787)

elif choice == 3:
   print(meters * 1.0936133)

else:
   print("Невірний вибір")

