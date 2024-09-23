# Введення розміру масиву
n = int(input("Введіть кількість елементів масиву: "))

# Введення елементів масиву
array = []
for i in range(n):
    element = int(input(f"Введіть елемент {i + 1}: "))
    array.append(element)

# Виведення введеного масиву
print("\nВведений масив:")
for i in range(n):
    print(array[i], end=" ")

# Виведення масиву у зворотному порядку
print("\n\nМасив у зворотному порядку:")
for i in range(n-1, -1, -1):
    print(array[i], end=" ")