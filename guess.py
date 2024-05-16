import random 
# Returns list of digits 
# of a number 
def getDigits(num): 
	return [int(i) for i in str(num)] 
# Returns True if number has 
# no duplicate digits 
# otherwise False	 
def noDuplicates(num): 
	num_li = getDigits(num) 
	if len(num_li) == len(set(num_li)): 
		return True
	else: 
		return False
# Generates a 4 digit number 
# with no repeated digits	 
def generateNum(): 
	while True: 
		num = random.randint(1000,9999)
		if noDuplicates(num): 
			return num 
# Returns common digits with exact 
# matches (placed) and the common 
# digits in wrong position (true) 
def numOfplacedtrue(num,guess): 
	placed_true = [0,0] 
	num_li = getDigits(num) 
	guess_li = getDigits(guess) 
	for i,j in zip(num_li,guess_li): 
		# common digit present 
		if j in num_li: 
			# common digit exact match 
			if j == i: 
				placed_true[0] += 1
			# common digit match but in wrong position 
			else: 
				placed_true[1] += 1
	return placed_true 
num = generateNum() 
tries =int(input('Enter number of tries: ')) 
# Play game until correct guess 
# or till no tries left 
while tries > 0: 
	guess = int(input("Enter your guess: ")) 
	if not noDuplicates(guess): 
		print("Number should not have repeated digits. Try again.") 
		continue
	if guess < 1000 or guess > 9999: 
		print("Enter 4 digit number only. Try again.") 
		continue
	placed_true = numOfplacedtrue(num,guess) 
	print(f"{placed_true[0]} placed, {placed_true[1]} true") 
	tries -=1
	if placed_true[0] == 4: 
		print("congratulation")
		print("You guessed right!") 
		break
else: 
	print(f"You ran out of tries. Number was {num}")