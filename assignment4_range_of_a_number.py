def test_range(n):
    if n in range(1,100):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range:")
n=int(input("give the number to find range : "))
test_range(n)