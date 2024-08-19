#Write some code using what you have learnt about the modulo operator
#and conditional checks in Python to check if the number in he input 
#area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".
print("Odd Vs. Even")
alpha = int(input ("Input an integer: \n"))
if (alpha % 2 == 0):
    print("This number is an odd number")
else:
    print("This number is an even number")