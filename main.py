a, b, c = int(input()), int(input()), int(input())

if (a+b<=c or a+c<=b or b+c<=a):
    print("треугольника не существует")

elif (c*c == a*a + b*b) or (a*a == b*b + c*c) or (b*b == a*a + c*c):
    print("прямоугольный")
    if (a==b or a==c or b==c):
        print("равнобедренный")
        if (c*c < a*a + b*b) or (a*a < b*b + c*c) or (b*b < a*a + c*c):
            print("острый")
        elif (c*c > a*a + b*b) or (a*a > b*b + c*c) or (b*b > a*a + c*c):
            print("тупой")

elif (a==b==c):
    print("равносторонний")

elif (a==b or a==c or b==c):
    print("равнобедренный")
    if (c*c < a*a + b*b) or (a*a < b*b + c*c) or (b*b < a*a + c*c):
        print("острый")
    elif (c*c > a*a + b*b) or (a*a > b*b + c*c) or (b*b > a*a + c*c):
        print("тупой")

elif (c*c < a*a + b*b) or (a*a < b*b + c*c) or (b*b < a*a + c*c):
    print("острый")

elif (c*c > a*a + b*b) or (a*a > b*b + c*c) or (b*b > a*a + c*c):
    print("тупой")
