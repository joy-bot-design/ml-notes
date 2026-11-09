#This program converts dollars to cedis
amount=float(input("Enter the amount in dollars: "))

#Conversion rate: 1 dollar = 15.50 cedis
rate=15.50

#Convert dollars to cedis
cedis=amount*rate
print(f"GHS: {cedis:,.2f}")