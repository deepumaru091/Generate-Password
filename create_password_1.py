# -*- coding: utf-8 -*-
"""CREATE PASSWORD 1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17qB6G4xjOBxLX7-bt1bmD8pa1TQyMG1K
"""

import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
#characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
characters = list(string.digits + string.ascii_letters+ "!@#$%^&*()")

def generate_random_password():
	## length of password from the user
	length = int(input("Enter password length: "))

	## number of character types
	alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(input("Enter special characters count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	password = []

	for i in range(alphabets_count):
		password.append(random.choice(alphabets))

	for i in range(digits_count):
		password.append(random.choice(digits))

	for i in range(special_characters_count):
		password.append(random.choice(special_characters))

	if characters_count < length:
		print("Characters total count is less than the password length")
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))

	if characters_count > length:
		print("Characters total count is greater than the password length")
		random.shuffle(characters)
	#	for i in range(characters_count - length):
		#	password.append(random.choice(characters))

	random.shuffle(password)
	print("".join(password))
generate_random_password()