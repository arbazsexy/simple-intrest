import sys
if len(sys.argv) >= 4:
    p = float(sys.argv[1])
    i = float(sys.argv[2])
    t = float(sys.argv[3])
else:
    p = float(input("Enter Principle: "))
    i = float(input("Enter intrest rate: "))
    t = float(input("Enter time: "))

si = p * i * t / 100

print("Simple intrest:", si)