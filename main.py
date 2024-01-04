print("Hello world")
################### 1 ######################

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

operation = input("ввести 'max', 'min', или 'average': ")
if operation == 'max':
    result = max(num1, num2, num3)
    print("максимальне значення:", result)
elif operation == 'min':
    result = min(num1, num2, num3)
    print("мінімальне значення:", result)
elif operation == 'average':
    result = (num1 + num2 + num3) / 3
    print("середне значення:", result)
else:
    print("Введена неприпустима операція. Будь ласка повторіть 'max', 'min', or 'average'.")

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

