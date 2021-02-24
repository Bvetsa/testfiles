user_number = int(input("Give me a number. "))

def even_func():
    if user_number % 2 or user_number == 0:
        print("Even number")
    else:
        print("ERROR!")

even_func()