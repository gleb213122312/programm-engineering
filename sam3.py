import math

one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

def triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return 0
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return area

a1 = max(one)
b1 = max(two)
c1 = max(three)

a2 = min(one)
b2 = min(two)
c2 = min(three)

area_max = triangle_area(a1, b1, c1)
area_min = triangle_area(a2, b2, c2)

print("Площадь треугольника из максимумов:", round(area_max, 3))
print("Площадь треугольника из минимумов:", round(area_min, 3))
