#encrypt function
def encrypt(alp, salp, num, a, b):

	text = ""
	while a < len(scr):
		#Number
		if (scr[a] in num) == True:
			for b in range(len(num)):
				if scr[a] == num[b]:
					text += num[(b+key)%len(num)]
				b += 1
		#Special character
		elif (scr[a] in schar) == True:
			for b in range(len(schar)):
				if scr[a] == schar[b]:
					text += schar[(b+key)%len(schar)]
				b += 1
		#Another character
		else:
			for b in range(len(alp)):
				if (scr[a] in alp) == False and (scr[a] in salp) == False:
					text += scr[a]
					break
				elif scr[a] == alp[b].upper():
					text += alp[(b+key)%len(alp)].upper()
				elif scr[a] == alp[b]:
					text += alp[(b+key)%len(alp)]
				b += 1
		b = 0
		a += 1
	return text

#decrypt function
def decrypt(alp, salp, num, a, b):

	text = ""
	while a < len(scr):
		#Number
		if (scr[a] in num) == True:
			for b in range(len(num)):
				if scr[a] == num[b]:
					text += num[(b-key)%len(num)]
				b += 1
		#Special character
		elif (scr[a] in schar) == True:
			for b in range(len(schar)):
				if scr[a] == schar[b]:
					text += schar[(b-key)%len(schar)]
				b += 1
		#Another character
		else:
			for b in range(len(alp)):
				if (scr[a] in alp) == False and (scr[a] in salp) == False:
					text += scr[a]
					break
				elif scr[a] == alp[b].upper():
					text += alp[(b-key)%len(alp)].upper()
				elif scr[a] == alp[b]:
					text += alp[(b-key)%len(alp)]
				b += 1
		b = 0
		a += 1
	return text

class class_inp():
	def def_scr(self):
		scr = input("Enter a script: ")
		return scr

	def def_key(self):
		while True:
			try:
				key = int(input("Enter a key: "))
				break
			except ValueError:
				print (" [!] Key must be an integer, please try again...\n")
		return key

#main
choice = 0
while (choice != "ex"):
	#Characters
	var = 0
	alp = "abcdefghijklmnopqrstuvwxyz"
	salp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	num = "0123456789"
	schar = """!@#$%^&*()-=[]\;'/_+{\}:"<>?"""
	guess = [" an "," am "," is "," are ","the "," will "," he "," she "," you "," was"," were"," in "," on "," at ","this ","that ",
	"these ","those ","have "," has "," and "," or "," want "," would ","very ","like ","what","which ","how","who","where","when"]
	a = 0
	b = 0
	choice = input("You want to encrypt, decrypt, bruteforce or exit? (en/de/brf/ex): ")
	inp = class_inp()

	#encrypt
	if choice == "en":
		scr = inp.def_scr()
		key = inp.def_key()

		print ("")
		print ("Your script has been encrypted (key = %d):" % key)
		print ("--------------------------------------------------------------------------------")
		var = encrypt(alp, salp, num, a, b)
		print (var)
		print ("--------------------------------------------------------------------------------\n")

	#decrypt
	elif choice == "de":
		scr = inp.def_scr()
		key = inp.def_key()

		print ("")
		print ("Your script has been decrypted (key = %d):" % key)
		print ("--------------------------------------------------------------------------------")
		var = decrypt(alp, salp, num, a, b)
		print (var)
		print ("--------------------------------------------------------------------------------\n")

	#bruteforce
	elif choice == "brf":
		scr = inp.def_scr()
		key = 1
		print ("")
		print ("--------------------------------------------------------------------------------")
		while (key <= 25):
			var = decrypt(alp, salp, num, a, b)
			print ("[key=%d]" % key, var, end="")
			for count in guess:
				if (count or count.upper()) in var:
					print(" (*) ", end="")
					break
			print("\n", end="")
			key += 1
		print ("--------------------------------------------------------------------------------")
		print ("(*): Recommend script for you\n")

	#exit
	elif choice == "ex":
		print ("Goodbye!, see you next time :)")

	#wrong input
	else:
		print (" [!] Wrong input, please try again...\n")