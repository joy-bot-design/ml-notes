#This program splits the bill among friends
total=float(input("Enter the total bill amount: "))
friends=int(input("Enter the number of friends: "))
bill_per_person=total/friends

print(f"Each person should pay: GHS {bill_per_person:,.2f}")

#printing 10% increase of each person
tip_per_person=bill_per_person*0.10

#printing each person total amount to pay after including tip
total_per_person=bill_per_person+tip_per_person
print(f"Each person should pay a total of after including 10% tip: GHS {total_per_person:,.2f}")
