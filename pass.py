
acc_name = input(" For Which Account You Need Password? : ")

import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 16)))
print ("The Password is = ", password)
