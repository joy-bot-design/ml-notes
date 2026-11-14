def main():
    a = float(input("Enter the value of a "))
    b = float(input("Enter the value of b "))
    print(f"The hypotenuse is: {hypotenuse(a, b)}")
    result = a * b
    return result

def square(n):
    return n**2

def hypotenuse(a, b):
    return (a**2 + b**2)**0.5

main()