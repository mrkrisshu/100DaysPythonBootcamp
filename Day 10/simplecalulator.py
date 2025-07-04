a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Choose operation (1/2/3/4): ")

if choice == "1":
    print("Result:", a + b)
elif choice == "2":
    print("Result:", a - b)
elif choice == "3":
    print("Result:", a * b)
elif choice == "4":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid choice.")
