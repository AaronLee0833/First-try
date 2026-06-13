shape1 = 0
shape2 = 0
shape3 = 0
shape4 = 0

print("==================")
print("Area Calculator 📐")
print("==================")

print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

shape = (int(input("Which shape: ")))

if shape == 1:
    base = int(input("Base: "))
    height = int(input("Height: "))
    shape1 = (height * base) / 2
    print("The area is: " + str(shape))

elif shape == 2:
    length= (int(input("Length:")))
    width = (int(input("Width:")))
    shape2 = (length * width)
    print("The area is: " + str(shape2))

elif shape == 3:
    side = (int(input("Side:")))
    shape3 = (side**2)
    print("The area is: " + str(shape3))

elif shape == 4:
    radius = (int(input("Radius:")))      
    π = 3.14
    shape4 = (π*radius**2)
    print("The area is: " + str(shape4))

elif shape == 5:
    print("Goodbye!")

else:
    print("Error: Invalid shape selection. Please choose a number between 1 and 5.")