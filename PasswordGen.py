import random
import string

character = ["!", "#", "@", "$", "%", "&", "(", ")"]
numb = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
         "w", "x", "y", "z"]
space = [" "]

value = int(input("How many characters would you like to set your password to? Choose between 8 and 128: "))

all = character + numb + alpha

ran = random.sample(all,value)

password = "".join(ran)

print(password)



