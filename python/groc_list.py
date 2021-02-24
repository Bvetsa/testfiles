
user_input = (input("Give me an input: "))
words =  len(user_input.split())
user_input_upper = user_input.upper()
user_input_lower = user_input.lower()
user_input_cap = user_input.title()
user_input_reverse = user_input[::-1]
user_input_char = len(user_input)


def print_data():
    print("\n")
    print("Your original statement was '" + user_input + "'.")
    print("There are " + str(words) + " words in your statement.")
    print("Your statement uppercased is '" + user_input_upper + "'.")
    print("Your statement lowercased is '" + user_input_lower + "'.")
    print("Your statement with only the first character in each word capitalized is '" + user_input_cap + "'.")
    print("Your statement reversed is '" + user_input_reverse + "'.")
    print("Your statement has " + str(user_input_char) + " characters.")
    print("\n")


print_data()