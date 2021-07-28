import random;
import string;

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

gen = lower + upper + num + symbols

lenght = 16

password = "".join(random.sample(gen, lenght))

print(password)