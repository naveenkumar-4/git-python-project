def check_palindrome(s):
	is s[::-1] == s:
		return True
	return False
s = input()
if check_palindrome(s) == True:
	print("Palindrome")
else:
	print("Not Palindrome")