# Two number :
"""" Developer usually use raise Exception to stop the code if the condition meet. """

input_1 = int(input("Enter a number : "))
input_2 = int(input("Enter a number : "))
if input_1 > input_2:
    raise Exception("first number can be larger than the second number.")
print((input_1 + input_2))
# assert :
"""" assert is used to run the code if condition meets otherwise it will stop."""

input_1 = int(input("Enter a number : "))
input_2 = int(input("Enter a number : "))
assert input_1 > input_2
print((input_1 + input_2))


# try , except and return :
def div(x, y):
    try:
        result = x / y
    except:
        result = "Cannot divide by zero."


print(div(5, 2))
print(div(5, 0))
