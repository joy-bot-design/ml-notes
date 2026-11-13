

def main():
    dollars = float(input("Enter the amount in dollars: "))
    print(f"{dollars} dollars is equivalent to GHS {to_cedis(dollars):.2f}")
    
    
def to_cedis(dollars):
    return dollars * 15.5

main()