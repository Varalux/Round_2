# Question 3 :  
# Print the largest possible for the given string.  
 
# Sample Input:  
# Enter the number of string to be entered = 2  
# Enter the string1 : abdf  
# Enter the string2 : hafd 

def reversed_string(a_string):
    return a_string[::-1]

def question3():
	n = input("Enter the number of string to be entered = ")
	
	for x in range(int(n)):
		k = input("Enter the string"+str(x)+" : ")  
		kl = reversed_string(k)
		print("String"+str(x)+" : "+kl)
	return	

question3() 

