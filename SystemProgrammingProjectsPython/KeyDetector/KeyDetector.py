import Inputmanager
import random

Generatingcount = 5

def Main():
    print("Welcome to this program.");
    
    while True:
        inputs = GetInput()
        counter = 1
        
        print("Keys founded: ")

        #MAIN CORE
        for x in inputs:
            print(counter, ": " , Inputmanager.GetChar(x) , "(",x,")")
            counter+=1
        input()

def GetInput():
    inputs = list()
    counter = 1

    while True:
        print("Press \"g\" for generating random inputs.")
        print("Press \"i\" for entering inputs.")

        if input() == "i":
            print("Enter key code(", counter , "). Or \"q\" to finish.:")
            inp = input();

            if inp == "q":
                if counter == 0:
                    continue
                else:
                    return inputs
            else:
                try:
                    inputs.append(int(inp))
                    counter+=1
                except :
                    print("Invalid input!. Pleas Try again.")
        else:
            print("Generating random input number")
            return GenerateInput(Generatingcount)

def GenerateInput(count):
    generated = list()
    for i in range(count):
        generated.append(random.randrange(Inputmanager.CharactersCount))
    return generated

Main(); #Ali Mohammadi 1401\12\9

