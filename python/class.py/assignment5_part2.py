age1 = input("What is the first persons age? ")
age1 = int(age1)
age2 = input("What is the second persons age? ")
age2 = int(age2)
age3 = input("What is the third persons age? ")
age3 = int(age3)
if age1 > age2 and age2 > age3:
    print("The first person is oldest, and the third person is youngest.")
elif age1 > age3 and age3 > age2:
    print("The first person is oldest, and the second person is youngest.")
elif age2 > age1 and age1 > age3:
    print("The second person is oldest, and the third person is youngest.")
elif age2 > age3 and age3 > age1:
    print("The second person is oldest, and the first person is youngest.")
elif age3 > age2 and age2 > age1:
    print("The third person is oldest, and the first person is youngest.")
elif age3 > age1 and age1 > age2:
    print("The third person is oldest, and the second person is youngest.")