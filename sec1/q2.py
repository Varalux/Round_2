# Question 2 :  
# Print the following pattern for the given n:  
# Sample Input 1:  
# Enter the number = 3  
 
# Sample Output 2:  
 
# 1 6 5
#   2 4
#     3

def question2():
  kl = input("Enter the number: ") 
  
  for x in range(1,int(kl)+1):
    for xy in range(1,int(kl)+1):
      lk = 0
      if x == xy:
        print("%-4d"%xy,end='')
        lk += 1
      elif x < xy:
        print("%-4d"%lk,end='')
        lk += 1
      else:
        print("    ",end='')
    print()
  return
    

question2()