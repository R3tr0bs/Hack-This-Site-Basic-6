#####################################################
#AUTHOR: R3tr0
#DESTINY: encrypt password on hack this site basic 6
#DATE: 4/21/2020
#####################################################
"""
explainantion about the encryption:
every character will change by his location
the first character will not change
the second will be the char plus one (a - b)
the third will be the char plus two 
and so on...
"""



encrypted = "6g9ffgh?"
dec = ""
for i in range(len(encrypted)):
	num = ord(encrypted[i])
	dec += chr(num-i)
print(encrypted + ":" + dec)

