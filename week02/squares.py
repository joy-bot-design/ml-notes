def main():
    a = int(input("Enter the value of a "))
    b = int(input("Enter the value of b "))
    print(f"The sum of squares is: {sum_of_squares(a, b)}")
    result=a * b
    return result
    
def square(n):
    return n**2

def sum_of_squares(a, b):
    return square(a) + square(b)

main()