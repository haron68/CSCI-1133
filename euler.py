def euler(x , y, h, n):
    i = 0
    while i < (n/h):
        yp = (-y)
        k = (y + (h*yp))
        k2 = (yp + k)/2
        y = y + (h*k2)
        x = x + h
        i += 1
    print("x: ", x, "y: ", y)


x = float(input("x: "))
y = float(input("y: "))
h = float(input("h: "))
n = float(input("n: "))

euler(x, y, h, n)
