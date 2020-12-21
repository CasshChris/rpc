#This is a is a comment
#for some reason it still prints "hitti"
try:
	#vim is the name of the program
	def vim():
		#hitti is the name of the calculator
		print("This is hitti")
		print("Hello! This is a adding and subtracking calculator")
		#tupni is the starting input, it gets the user to interact with the program
		tupni = input('Type "START" ')
		if tupni == "start".capitalize:
			number1 = float(input("Give a number : "))
			number2 = float(input("Give another number : "))
			numsum = number1 + number2
			x = 1
			if x == 1:
				print(numsum)
				yum = 0
				while yum <= 5:
					print("!!!thank you for testing!!!	!!!thank you for testing!!!	!!!thank you for testing!!!")
					yum += 1
		elif tupni != "START":
			#yum is a counter var
			yum = 0
			while yum <= 200:
				print("!!!thank you for testing!!!	!!!thank you for testing!!!	!!!thank you for testing!!!")
				yum += 1
	vim()
except:
	print('This is a error! ...not 404 tho')