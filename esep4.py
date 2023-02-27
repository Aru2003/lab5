numbers = []
while True:
    num = int(input("Введите число (0 для завершения ввода): "))
    if num == 0:
        break
    numbers.append(num)

numbers.sort(reverse=True)

print("Введенные числа в порядке убывания: ")
for num in numbers:
    print(num)