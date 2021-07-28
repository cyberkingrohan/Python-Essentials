#Random OTP generator using Python
import random as r
import string
length = 10
otp = ''

characters = string.ascii_letters + string.digits
for i in range(length):
    otp = otp + r.choice(characters)

print("Your Random OTP is :", otp)
