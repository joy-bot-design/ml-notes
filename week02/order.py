#print C B A D in that order

def first():
    print ("A")
    
    
def second():
    print ("B")
    first() 
    
    
print("C")
second()
print("D")