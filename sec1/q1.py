# Question 1:  
# Display the diagonal pattern for the string of odd length.  

# Sample Input 1:  
# Enter the string : try
 
# Sample Output 2:  
#     r
# t       y
#     r     

import math
def question1():
	s = input("Enter the string: ") 

	slen = len(s)

	if(len(s)%2==0):
		print("Not Possible...")
		question1()
	else:   
		mid = math.floor(slen/2)
		i = j = mid
		is_rev = False
		while True:
			if (i == j):
			  print('{}{}{}'.format(" "*i,s[i]," "*i))
			if is_rev:
			  i = i + 1
			  j = j - 1
			else:
			  i = i - 1
			  j = j + 1
			if (i == j):
			  print('{}{}{}'.format(" "*i,s[i]," "*i))
			else:
			  print('{}{}{}{}'.format(" "*i,s[i]," "*(j-i-1),s[j]," "*i))
			if (i == 0):
			  is_rev = True
			if (i == j):
			  break
		return  

question1()
