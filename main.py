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


