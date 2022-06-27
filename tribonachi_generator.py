def generator_function():
    t1 = t2 = 0
    t3 = 1
    while True:
        t1, t2, t3 = t2, t3, t1 + t2 + t3
        yield t3

number = int(input("Введите количество чисел"))
gen = generator_function()
for i in range(number):
    if i == 0:
        print(0)
    elif i == 1:
        print(0)
    elif i == 2:
        print(1)
    else:
        print(next(gen))
