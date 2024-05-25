binary=input("Enter Binary number : ")
try:
    dicemal = int(binary , 2)
    print ("the dicemal of", binary,"is",dicemal)
except ValueError:
    print("invalid input the number must be binary number")
