'''
Question: Check whether three sides form a right-angled triangle.
'''

a = int(input("Enter side a (cm): "))
b = int(input("Enter side b (cm): "))
c = int(input("Enter side c (cm): "))

def is_right_triangle(base, height, hypotenuse):
    return hypotenuse**2 == base**2 + height**2

if a + b > c and a + c > b and b + c > a:

    if c >= a and c >= b:
        result = is_right_triangle(a, b, c)
    elif b >= a and b >= c:
        result = is_right_triangle(a, c, b)
    else:
        result = is_right_triangle(b, c, a)

    if result:
        print("It's a right-angled triangle.")
    else:
        print("It's NOT a right-angled triangle.")

else:
    print("INVALID triangle sides.")


