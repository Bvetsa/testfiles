groc_list = {}

def restart():
    restart = input("would you like to add another item?(y/n): ")
    if restart == 'Y' or restart == 'y':
        groc_func()
    else:
        print(groc_list)


def groc_func():
    groc_list[input("What is the item you would like: ")] = input("how many of your item would you like: ")
    restart()


groc_func()

