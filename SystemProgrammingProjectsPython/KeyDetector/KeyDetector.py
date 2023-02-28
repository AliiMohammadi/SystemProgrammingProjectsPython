import Inputmanager

def Main():
    print("Welcome to this program.");
    
    while True:
        inputs = GetInput()
        counter = 1

        print("Keys founded: ")

        for x in inputs:
            print(counter, ": " , Inputmanager.GetChar(x) , "(",x,")")
            counter+=1

def GetInput():
    inputs = list()
    counter = 1

    while True:
        print("Enter key code(", counter , "). Or |q| to finish.:")
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

Main(); #Ali Mohammadi 1401\12\9

