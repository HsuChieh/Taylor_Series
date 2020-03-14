a = float(input("a"))
b = float(input("b"))
c = float(input("c"))
d = float(input("d"))
print("the derivative of")
if a == 1:
    print("(", c, "x - ", d, ")**",b)
else:
    print(a,"(", c, "x - ", d, ")**",b)
print("is")
a = a*b*c
b -= 1
if b == 0:
    print("1")
elif a == 1:
    print("(", c, "x)**",b)
elif b == 1:
    print(a, "(", c, "x)")
elif a == 1 and b == 1:
    print( c, "x")
else:
    print(a,"(", c, "x)**",b)
