num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
armstrong = sum(d ** power for d in digits)

if num == armstrong:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
