def add_tip(bill):
    total= bill * 1.1
    return total
    
total = add_tip(100)
print(f"Total:{total:.2f}")