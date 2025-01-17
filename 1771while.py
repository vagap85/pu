multipl = 1
num = 1
while num <= 10:
    if num % 2 != 0:
        multipl *= num
    num += 1
print("Произведение всех нечётных чисел от 1 до 10:", multipl)