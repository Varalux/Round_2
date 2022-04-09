# Question 7: 
# Print the distinct words in the given string.  
 
# Sample Input 1:  
# Enter the string : This is Zoho and Zoho is good  
 
# Sample Output 1:  
# The distinct words are : This is Zoho and good  

def question7():
	n = input("Enter the string : ")
	
	lk = ''
	n = n.split(' ')
	for ff in n:
		if str(ff) in lk.split(' '):
			print(ff)
			pass
		else:
			lk += ff+' '
	print("The distinct words are : ",lk)

question7()