'''
def divfunc():
    for x in range(1, 17000):
        if x % 1001 != 0:
            print(x)
        else:
            pass

divfunc()


def is_divisable(x,y):
    if x % y == 0:
        return True
    else:
        return False

print(\
    is_divisable(
        int(input("Give me a number: \n")),\
        int(input("Give me another number: \n"))\
    )
)
'''
def perf_sq():
    import math
    number = int(input("Enter the Number: "))

    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        print(number, "is a perfect square")
    else:
        print(number," is not a perfect square")    

perf_sq()