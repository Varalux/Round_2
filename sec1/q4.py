# Question 4:  
# Print the following pattern for the given input.  
 
# Input:  
# Enter the number : 5  
 
# Output:
 
 
# 5 5 5 5 5 5 5 5 5  
# 5 4 4 4 4 4 4 4 5  
# 5 4 3 3 3 3 3 4 5  
# 5 4 3 2 2 2 3 4 5  
# 5 4 3 2 1 2 3 4 5  
# 5 4 3 2 2 2 3 4 5  
# 5 4 3 3 3 3 3 4 5  
# 5 4 4 4 4 4 4 4 5  
# 5 5 5 5 5 5 5 5 5  

def question4():
	n = int(input("Enter the number = "))
	
	level=n+n-1
	for i in range(0,level):
	  x=n+1
	  for j in range(0,level):
	    if (i<=(level/2)):
	      if (j+i>=level):
	        x = x + 1
	      elif (j<=i):
	        x = x - 1
	    elif (i>(level/2)):
	      if (j+i<level):
	        x = x - 1
	      if (j>i):
	        x = x + 1
	    print('{}'.format(x),end=" ")
	  print("")

question4() 