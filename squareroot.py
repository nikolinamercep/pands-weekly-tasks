#squareroot.py
#program takes a number and calculates the square root
#author chatGPT, no idea why or how it works
#will work on it later

def square_root_approximation(number):
    if number < 0:
        return "Square root is undefined for negative numbers"
    
    # Initial guess for the square root
    guess = number / 2.0
    
    # Iterate until convergence
    while True:
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < 0.0001:  # Adjust the threshold for desired precision
            break
        guess = new_guess
    
    return new_guess

def main():
    # Take input from the user
    number = float(input("Please enter a positive number: "))
    
    # Calculate and print the approximation of square root
    approximation = square_root_approximation(number)
    print("Approximation of square root:", approximation)

if __name__ == "__main__":
    main()
