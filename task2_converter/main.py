"""Перевод расстояния между заданными единицами измерения."""

to_metres = {
    "km": 1000,
    "m": 1,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
}

source_unit = input("Исходная единица (km, m, cm, mm, mi, yd): ").lower()
target_unit = input("Целевая единица (km, m, cm, mm, mi, yd): ").lower()

if source_unit in to_metres and target_unit in to_metres:
    value = float(input("Введите расстояние: "))
    result = value * to_metres[source_unit] / to_metres[target_unit]
    print(f"Результат: {result:.6g} {target_unit}")
else:
    print("Неизвестная единица измерения")
