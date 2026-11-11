x=input("Number? ")

print(type(x))

print(x+x)

#input() always gives text
#it sees it as a text and not an integer


print("Kumasi", "Accra", "Tamale", sep="|")

print("loading", end="...")
print("ready")


#sep="|" puts | between them
#end="..." stops print() from starting a new line
#ready is on the same line because of the end="..."


print("["+"   Akwaaba   ".strip() +"]")

#AttributeError: 'str' object has no attribute 'stripe'. Did you mean '.strip' instead of '.stripe'?