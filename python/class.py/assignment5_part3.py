gender = input("What is your gender? (Please enter male or female) ")
age = input("How old are you? ")
female = ("female")
male = ("male")
age = int(age)

if gender == female and age > 10 and age < 15:
    print("You may own an iPad")
elif gender == male and age > 10 and age < 15:
    print("You may own an iPad")
elif gender == female or gender == male and age < 10:
    print("You may borrow an iPad")
else:
    print("ERROR!")