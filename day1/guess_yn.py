# Author:Jim Dai
age_of_me= 27

count = 0
while count < 3:
	guess_age = int(input("guess age: "))

	if guess_age == age_of_me:
		print("Yes, you are right!")
		break
	elif guess_age < age_of_me:
		print("guess higher")
	else:
		print("guess smaller")

	count+=1
	if count == 3:
		while True:
			confirm = input("Do you want to replay? [y/n]: ")
			if confirm == 'y':
				count = 0
				break
			elif confirm == 'n':
				print("Bye!")
				exit()
			else:
				print("Wrong input!")
				#continue
