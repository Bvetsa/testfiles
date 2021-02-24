
import random

upper_letter1 = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
upper_letter2 = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
lower_letter1 = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
lower_letter2 = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
digit1 = ("0", "1", "2", "3", "4", "5","6","7","8","9")
digit2 = ("0", "1", "2", "3", "4", "5","6","7","8","9")
punc = ("?","!","#","$","%","^","&","*","(",")")
random_upper1 = random.choice(upper_letter1)
random_upper2 = random.choice(upper_letter2)
random_lower1 = random.choice(lower_letter1)
random_lower2 = random.choice(lower_letter2)
random_digit1 = random.choice(digit1)
random_digit2 = random.choice(digit2)
random_punc = random.choice(punc)
random_stuff = (random_upper1,random_upper2,random_lower1,random_lower2,random_digit1,random_digit2,random_punc)

random_stuff = list(random_stuff)
random.shuffle(random_stuff)
print(random_stuff)

