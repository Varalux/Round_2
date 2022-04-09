# Question 1:  
# Display the diagonal pattern for the string of odd length.  

# Sample Input 1:  
# Enter the string : try
 
# Sample Output 2:  
#     r
# t       y
#     r     

def question1():
  kl = input("Enter the string: ") 

  if(len(kl)%2==0):
    print("Not Possible...")
    question1()
  else:   
    n = int(len(kl))
    row = 1
    while row <= n:
        col = 1
        while col <= n:
            print(kl[col-1],''*col,end ='')
            col += 1
        print()        
        row+=1
        pass
    return

question1()