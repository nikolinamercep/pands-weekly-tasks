# collatz.py
# asks user to input a positive integer
# if even, divides by 2
# if odd, multiplies by 3 and adds 1
# prints the results until the result is 1

number = int(input("Please enter any positive integer: "))

while number != 1:
    if (number % 2) == 0:
        number /= 2
    else:
        number *= 3
        number += 1
    print (number)
