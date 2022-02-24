# Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is greater than 1000, else return their sum


# declaring function
def calculator(a, b):
    product = a*b # calculate the product of the two numbers

    if product <= 1000: # check to see if product is less that 1000
        return product
    else:
        return a + b # product is greate 1000, calculate sum.

# calling function - first condition
result = calculator(20,30)
print("The result is: " ,result)
print()

# calling function - second condition
result = calculator(40,30)
print("The result is: ", result)



