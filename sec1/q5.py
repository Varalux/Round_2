# Question 5:
# Check whether the given string has characters of equal difference or unequal difference.

# Sample Input 1:
# 	Enter the string : abcdefg
# Sample Output 1:
# Equal difference.

# Sample Input 2:
# 	Enter the string : adxz
# Sample Output 2:
# 	Unequal difference.

def question5():
	n = input("Enter the string : ")

	jk = 1
	succ = False
	for x in range(len(n)):	
		if x<round(len(n)/2)+1:
			kk = abs(ord(n[x+1]) - ord(n[x]))
			ll = abs(ord(n[-jk-1]) - ord(n[-jk]))
			if kk == 1 and ll == 1:	
				succ = True
		jk+=1

	if succ is True:
		print("Equal difference.")
	else:
		print("Unequal difference.")

question5() 