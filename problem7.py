num = int(input("Enter your number:"))

if num % 3 == 0 and num % 5==0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5==0:
    print("Buzz")
else:
    print("Not a fizz-buzz number")