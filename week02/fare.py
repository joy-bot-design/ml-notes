def main():
    stops = int(input("Enter the number of stops: "))
    total = fare(stops,3)
    print(f"Fare: GHS{total:.2f}")
    
    


def fare(stops, price=2.5):
    return stops * price


main()