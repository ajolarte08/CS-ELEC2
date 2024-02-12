try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    result = 10 / number
    print("Result:", result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Division successful!")

