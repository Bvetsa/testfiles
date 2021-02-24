
'''
def is_square(number):
    for counter in range(1,number):
        if counter * counter == number:
            return True
    
    return False

def is_cube(number):
    for counter in range(1,number):
        if counter * counter * counter == number:
            return True

    return False

def is_fourth_power(number):
    for counter in range(1,number):
        if counter * counter * counter * counter * counter == number:
            return True

    return False
def print_num(ends):
    for x in range(0,int(ends)):
        if is_square(x) or is_cube(x) or is_fourth_power(x):
            print(x)
        else:
            continue

print_num(input("Till what number do you want this to go to? \n"))
'''

'''
func(number1,number2)
if number1 is a perfect power of number2, then print number1
in other words, if number1 is equal to nth exponent of number2, then print number1, else print "not a perfect power"
func(8,2) - 8 is 2 cubed; so print 8
func(4,2) - 4 is 2 squared, so print 4
func(9,3) - 9 is 3 squared, so print 9
func(9,2) - skip, 9 is not an exponent of 2
func(16,2) - 16 is 2 power 4, so print 16
func(625,5) - 625 is exponent of 5, 625 is 4th power of 5, so print 625
'''

def is_power():
    