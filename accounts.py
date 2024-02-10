# accounts.py
# asks to input 10 digit account number 
# outputs only the last 4 digits showing (and the first 6 digits replaced with Xs)
input_number = input("Please enter a 10-digit account number: ")
output_number = 'X' * 6 + input_number[-4:]
print(output_number)