# Question 6: 
# Find one of the maximum possible palindrome in the given string.  
 
# Input:  
# Enter the string : madameaga  
 
# Output:  
 
# aamdmaa  


from collections import defaultdict
 
 
def get_Palindrome(st):
 
    # Store counts of characters
    smaph = defaultdict(int)
    for i in range(len(st)):
        smaph[st[i]] += 1
 
    # Find the number of odd elements.
    # Takes O(n)
    odd_Count = 0
 
    for x in smaph:
        if (smaph[x] % 2 != 0):
            odd_Count += 1
            odd_Char = x

    # print(odd_Count,odd_Char,smaph)
    # odd_cnt = 1 only if the length of str is odd
    if (odd_Count > 1 or odd_Count == 1 and len(st) % 2 == 0):
        return "NO PALINDROME"
 
    # Generate first halh of palindrome
    firstHalf = ""
    secondHalf = ""
 
    for x in sorted(smaph.keys()):
 
        # Build a string of floor(count/2) occurrences of current character
        s = (smaph[x] // 2) * x
 
        # Attach the built string to end of and begin of second half
        firstHalf = firstHalf + s
        secondHalf = s + secondHalf
 
    # Insert odd character if there is any
    if (odd_Count == 1):
        return (firstHalf + odd_Char + secondHalf)
    else:
        return (firstHalf + secondHalf)



def question6():
    n = input("Enter the string : ")

    s_list = []
    palindrom_lt = str(n)

    for x in range(len(n)): 
        lk = n.count(n[x])
        if lk == 1:
            palindrom_lt= palindrom_lt.replace(str(n[x]), "")
            s_list.append(n[x]) 
        elif lk%2 != 0:
            palindrom_lt = palindrom_lt.replace(str(n[x]), "")

    # print(s_list)
    # print(palindrom_lt)

    if s_list:
        palindrom_lt+= s_list[0] 

    print("Possible Palindrome : ",get_Palindrome(palindrom_lt))
    return

question6()



    