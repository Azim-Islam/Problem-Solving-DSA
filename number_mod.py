# Python 3 program to find quotient and remainder 
# when a number is divided by large number 
# represented as string. 

# Function to calculate the modulus 
def modBigNumber(num, m): 
	# Store the modulus of big number 
	vec = [] 
	mod = 0

	# Do step by step division 
	for i in range(0,len(num),1): 
		digit = ord(num[i]) - ord('0') 

		# Update modulo by concatenating 
		# current digit. 
		mod = mod * 10 + digit 

		# Update quotient 
		quo = int(mod / m) 
		vec.append(quo) 

		# Update mod for next iteration. 
		mod = mod % m	 
	
	#print("\n") 
	print(mod) 


	# Flag used to remove starting zeros 
	zeroflag = 0; 
	for i in range(0,len(vec),1): 
		if (vec[i] == 0 and zeroflag == 0): 
			continue
		zeroflag = 1
		#print(vec[i],end="") 

	return

# Driver Code 

num = input()
m = int(input())
modBigNumber(num, m) 

# This code is contributed by 
# Surendra_Gangwar 
	
