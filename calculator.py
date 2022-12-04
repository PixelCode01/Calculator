print("Calculater")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
o=int(input("Enter Choice 1-4:"))
if o==1:
	a=int(input("Enter A:"))
	b=int(input("Enter B:"))
	c=a+b
	print("Sum = ",c)
elif o==2:
	a=int(input("Enter A:"))
	b=int(input("Enter B:"))
	c=a-b
	print("Subtraction = ",c)
elif o==3:
	a=int(input("Enter A:"))
	b=float(input("Enter B:"))
	c=a*b
	print("Product = ",c)
elif o==4:
	a=int(input("Enter A:"))
	b=int(input("Enter B:"))
	c=a/b
	print("Answer = ",c)
