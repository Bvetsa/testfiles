import graph_point


def restart():
    restart = input("\nDo you want to do another operation with the same points? (y/n)")

    if restart == 'y' or restart == 'Y':
        pick_func()
    else:
        exit


def pick_func():
    input_function = input("\nSelect which Function you wish to use by pressing the number corrosponding to the function: \n 1: Print Point \n 2: distance between point 2 and center \n 3: distance between points 1 and 2 \n 4: slope between 2 points \n 5: slope from center\n 6: area between 2 points\n 7: area from center\n 8: smallest angle\n 9: the y intercept\n")

    if input_function == '1':
        print(p1.print_point())
    elif input_function == '2':
        print(p2.distance_from_center())
    elif input_function == '3':
        print(p1.distance_from_another_point(p2))
    elif input_function == '4':
        print(p1.slope_between_2_points(p2))
    elif input_function == '5':
        print(p1.slope_from_center())
    elif input_function == '6':
        print(p1.area_from_another_point(p2))
    elif input_function == '7':
        print(p1.area_from_center())
    elif input_function == '8':
        print(p1.smallest_angle(p2))
    elif input_function == '9':
        print(p1.y_int(p2))
    restart()

pick_func()





