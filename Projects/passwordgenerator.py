import random

caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lows = "abcdefghijklmnopqrstuvwxyz"
special = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
LengthMenu = """Password Generator:
(Choose length)
1. 8  Characters
2. 12 Characters
3. 16 Characters
4. 18 Characters"""
CharMenu = """
(Choose included characters)
1. Capital letters    (ex: ABC...)
2. Lowercase letters  (ex: abc...)
3. Special characters (ex: !#$...)
(enter the numbers of the characters you want)"""

print(LengthMenu)
LengthInput = input('[>]   ')
if LengthInput == "1":
	length = 8
elif LengthInput == "2":
	length = 12
elif LengthInput == "3":
	length = 16
elif LengthInput == "4":
	length = 18
else:
	print("That's not an option, ending script now...")
	exit()

print(CharMenu)
CharInput = input('[>]   ')
for i in CharInput:
	if int(i) > 3:
		print("That's not an option, ending script now...")
		exit()

CharList = ""
if "1" in CharInput:
	CharList += caps
if "2" in CharInput:
	CharList += lows
if "3" in CharInput:
	CharList += special

FinalPassword = ""

for i in range(0, length):
	RandomLetter = random.choice(CharList)
	FinalPassword += RandomLetter

print('Generating.')
print('Generating..')
print('Generating...')
print(f"""Final Password:
{FinalPassword}""")
