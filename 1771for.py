multipl = 1
for num in range(1, 11):
    if num % 2 != 0:
        multipl *= num
print("Произведение всех нечётных чисел от 1 до 10:", multipl)