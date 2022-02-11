def fact(n):
	if(n==0):
		return(1)
	elif(n<0):
		print("factorial doesnt exist")
	else:
		return(n*fact(n-1))
a=int(input("Enter the number: "))
print(fact(a))
