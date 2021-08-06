# coding: utf-8

# """
# # encrypt(‘abc’,1) would return ‘bcd’ = E.g. encrypt(‘abc’, 10) would return ‘klm’

# encrypt(‘abc’,27) would return ‘bcd’

# encrypt(‘zzz’,1) would return ‘aaa’
# """

def encrypt(text, key):
	result = ""

	for i in range(len(text)):
		char = text[i]

		if (char.isupper()):
			result += chr((ord(char) + key - 65) % 26 + 65)

		else:
			result += chr((ord(char) + key - 97) % 26 + 97)

	return result

def decrypt(result, key):
	return encrypt(result, -key)

	
#check the above function
if __name__ == "__main__":

	input1 = "ABCD"
	input2 = "abcd"
	input3 = "ABab"
	input4 = "AB ab AB cd dfadf  fasdf"
	input5 = "Hello World. We did it."

result1 = encrypt(input4, 2)
print(result1)

  # result2 = decrypt(result1, 900)
  # print(result2)
