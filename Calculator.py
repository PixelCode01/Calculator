result = 0

while True:

  print("Calculator")

  print("1. Addition")

  print("2. Subtraction")

  print("3. Multiplication")

  print("4. Division")

  print("5. Exponentiation")

  print("6. Modulus")

  print("7. Use result from previous operation")

  print("8. Quit")

  operation = int(input("Enter a choice 1-8: "))

  if operation == 8:

    break

  elif operation == 7:

    num1 = result

    num2 = float(input("Enter number 2: "))

  else:

    num1 = float(input("Enter number 1: "))

    num2 = float(input("Enter number 2: "))

      

  if operation == 1:

    result = num1 + num2

  elif operation == 2:

    result = num1 - num2

  elif operation == 3:

    result = num1 * num2

  elif operation == 4:

    result = num1 / num2

  elif operation == 5:

    result = num1 ** num2

  elif operation == 6:

    result = num1 % num2

  

  print("Result: ", result)

