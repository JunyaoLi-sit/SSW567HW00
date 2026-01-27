# HW00b Triangle
# Junyao Li

def classify_Triangle(a, b, c):

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'
    elif ((a ** 2) + (b ** 2)) == (c ** 2) or \
         ((a ** 2) + (c ** 2)) == (b ** 2) or \
         ((b ** 2) + (c ** 2)) == (a ** 2):
        return 'Right'
    elif (a != b) and (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'


if __name__ == "__main__":
    try:
        a = int(input("Enter side a: "))
        b = int(input("Enter side b: "))
        c = int(input("Enter side c: "))

        print("Triangle type:", classify_Triangle(a, b, c))
    except ValueError:
        print("InvalidInput")
