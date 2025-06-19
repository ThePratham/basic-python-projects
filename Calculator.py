import math

print("\t\t<><><><><><><> CALCULATOR <><><><><><><>")

#------------------ Functions ------------------#

def sum_nums(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    remainder = a % b
    quotient = a / b
    return remainder, quotient

def sqrt(a):
    return math.sqrt(a)

def power(a, b):
    return a ** b

def sin_deg(a):
    return math.sin(math.radians(a))

#------------------ Main Program ------------------#

a1 = int(input("INPUT FIRST NUMBER: "))

print("What do you want to do with it?\n"
      "\t1. Addition (1 or +)\n"
      "\t2. Subtraction (2 or -)\n"
      "\t3. Multiplication (3 or *)\n"
      "\t4. Division (4 or /)\n"
      "\t5. Square root (5)\n"
      "\t6. Power (^) \n"
      "\t7. Sin (7 or sin)")

func = input("Enter the function's number or symbol: ")

# One number operations
if func == "5":
    print("The square root is:", sqrt(a1))

elif func == "7" or func.lower() == "sin":
    print("The sine of the number (degree) is:", sin_deg(a1))

# Two number operations
elif func in ["1", "+", "2", "-", "3", "*", "4", "/", "^"]:
    
    # Division with protection
    if func == "4" or func == "/":
        while True:
            b1 = int(input("Enter the second number (non-zero): "))
            if b1 == 0:
                print("DON'T TRY TO BE SMART — IT DOESN'T SUIT YOU. YOU THOUGHT I WOULDN’T THINK ABOUT THIS?")
            else:
                rem, quo = div(a1, b1)
                print("Remainder:", rem)
                print("Quotient:", quo)
                break

    else:
        b1 = int(input("Enter the second number: "))

        if func == "1" or func == "+":
            print("The result is:", sum_nums(a1, b1))

        elif func == "2" or func == "-":
            print("The result is:", sub(a1, b1))

        elif func == "3" or func == "*":
            print("The result is:", mul(a1, b1))

        elif func == "^":
            print("The result is:", power(a1, b1))

else:
    print("Invalid sign or input. Try something real, love.")

input("\nPress Enter to exit...")

# ~~~~ PROJECT BY PRATHAM (aka The augustine Coder) ~~~~
