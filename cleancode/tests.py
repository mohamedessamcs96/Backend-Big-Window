def nearest_square(num):
    """
    return the nearest square
    """
    root=0
    while(root+1)**2<=num:
        root+=1
    return root **2

def sumNumbers(x,y):
    return x+y

print("The nearest square for the 5 is:",nearest_square(5))
#assert(nearest_square(5)==4)
print("The nearest square for the 16 is:",nearest_square(16))
#assert(nearest_square(16)==16)
print("The nearest square for the 22 is:",nearest_square(22))
#assert(nearest_square(22)==16)
print("The nearest square for the 14 is:",nearest_square(14))
#assert(nearest_square(14)==16)
print("The nearest square for the 9 is:",nearest_square(9))
#assert(nearest_square(9)==9)


