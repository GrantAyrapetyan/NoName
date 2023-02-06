s = []
a = []
print("Hello world")
for i in range(-10, 10):
    if i % 2 == 0:
        s.append(i)
    elif i % 2 != 0:
        a.append(i)
print("Четный массив:", s)
print("Нечетный массив:", a)


