x = int(input("give me a number: "))
y = 2
z = x % y


while y <= x//2:
    if z == 0:
        print("Not Prime")
    if z != 0: 
        print ("Prime")
        y += 1
    z = x % y
    