# Charles Monaghan
def encode(password):
	encoded_pass = ''
	for char in password:
		encoded_val = int(char) + 3
		if encoded_val >= 10:
			encoded_val %= 10
		encoded_pass += str(encoded_val)
	return encoded_pass


def decode(password):
	var = ""
	for i in password:
		result = int(i)
		result -= 3
		if result < 0:
			result += 10
		var += str(result)
	return var


if __name__ == "__main__":
	while True:
		print('Menu')
		print('-------------')
		print('1. Encode')
		print('2. Decode')
		print('3. Quit')
		print()
		print('Please enter an option: ')
		choice = input()

		if choice == '1':
			user_pass = input('Please enter your password to encode:')
			encrypted_pass = encode(user_pass)
			print("Your password has been encoded and stored!")
		elif choice == '2':
			pass
		elif choice == '3':
			break
		else:
			print('Invalid option, please try again')
