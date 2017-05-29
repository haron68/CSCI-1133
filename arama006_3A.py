# CSci 1133-20 HW 3
# Haron Arama
# HW 3, Problem 3A

inputType = input("Are input components int or float (i/f)? ")

if inputType == "f":
    red     = float(input("Red component: ")) * 255
    green   = float(input("Green component: ")) * 255
    blue    = float(input("Blue component: ")) * 255

    rint = int(red)
    gint = int(green)
    bint = int(blue)

    if (red - rint) == 0.5:
        rint = rint + 1

    if (blue - bint) == 0.5:
        bint = bint + 1

    if (green - gint) == 0.5:
        gint = gint + 1

    print("Int representation: ", rint, gint, bint)
elif inputType == "i":
    red     = int(input("Red component: ")) / 255
    green   = int(input("Green component: ")) / 255
    blue    = int(input("Blue component: ")) / 255

    red = float("{0:.2f}".format(red))
    green = float("{0:.2f}".format(green))
    blue = float("{0:.2f}".format(blue))

    print("Float representation: ", red, green, blue)
else:
    print("Invalid option.")