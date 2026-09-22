"""Вычисление площади треугольника по формуле Герона."""

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    half_perimeter = (a + b + c) / 2
    area = (half_perimeter * (half_perimeter - a)
            * (half_perimeter - b) * (half_perimeter - c)) ** 0.5
    print(f"Площадь треугольника: {area:.2f}")
else:
    print("Треугольник с такими сторонами не существует")
