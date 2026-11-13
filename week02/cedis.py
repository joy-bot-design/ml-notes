#def is used to define a function in Python. 

#parameter is a variable written inside the parentheses in the function definition.

#an argument is the actual value that is passed to the function when it is called.


def main():
    amount=float(input("Enter the amount in dollars: "))
    print(f"GHS {to_cedis(amount):.2f}")
    


def to_cedis(amount):
    return amount*15.5
    
    
main()