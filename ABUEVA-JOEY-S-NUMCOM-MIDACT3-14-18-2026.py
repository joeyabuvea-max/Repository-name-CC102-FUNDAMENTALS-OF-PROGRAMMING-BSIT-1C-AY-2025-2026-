# ___________Number Ones___________
def ones(x):
    if x == 1: print("One", end=" ")
    elif x == 2: print("Two", end=" ")
    elif x == 3: print("Three", end=" ")
    elif x == 4: print("Four", end=" ")
    elif x == 5: print("Five", end=" ")
    elif x == 6: print("Six", end=" ")
    elif x == 7: print("Seven", end=" ")
    elif x == 8: print("Eight", end=" ")
    elif x == 9: print("Nine", end=" ")

# ___________Number Tens___________
def tens(x):
    if x == 1: print("Ten", end=" ")
    elif x == 2: print("Twenty", end=" ")
    elif x == 3: print("Thirty", end=" ")
    elif x == 4: print("Forty", end=" ")
    elif x == 5: print("Fifty", end=" ")
    elif x == 6: print("Sixty", end=" ")
    elif x == 7: print("Seventy", end=" ")
    elif x == 8: print("Eighty", end=" ")
    elif x == 9: print("Ninety", end=" ")

# # Main Program
num = int(input("Enter a number (0-9999): "))

if num == 0:
    print("Zero")
else:
    # Extract Thousands
    thousands_digit = num // 1000
    if thousands_digit > 0:
        ones(thousands_digit)
        print("Thousand", end=" ")

    # Extract Hundreds
    remainder = num % 1000
    hundreds_digit = remainder // 100
    if hundreds_digit > 0:
        ones(hundreds_digit)
        print("Hundred", end=" ")

    # Extract Tens
    remainder = remainder % 100
    tens_digit = remainder // 10
    if tens_digit > 0:
        tens(tens_digit)

    # Extract Ones
    ones_digit = remainder % 10
    if ones_digit > 0:
        ones(ones_digit)
    
    print() # New line at the end
