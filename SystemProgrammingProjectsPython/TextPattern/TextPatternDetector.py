def Main():
    userinput = GetInput()
    print("Founded strings:")
    for x in FindPattern("abc",userinput):
        print(x)
def GetInput():
    inputs = ""
    counter = 1

    while True:
        print("Enter line (", counter , "). Or 0 to finish.:")
        inp = input();

        if inp == "0":
            if counter == 0:
                continue
            else:
                return inputs
        else:
            try:
                inputs += inp
                counter+=1
            except :
                print("Invalid input!. Pleas Try again.")

#Scanning prameter text in order to find similar strings to the prameter pattern
def FindPattern(pattern, text):
    founded = list()
    stack = ""

    started = pattern[0]
    targets = pattern[1]
    end = pattern[len(pattern) - 1]

    for x in text:
        if(x != started and x!=end and x != targets):
            stack = ""
        else:
            length = len(stack)

            if(x == started):
                if(length == 0):
                    stack += x
                else:
                    stack = ""
            if(x == targets) and (length > 0):
                stack += x
            if(x == end):
                if(length > 0):
                    stack += x
                    founded.append(stack)
                    stack = ""
    return founded

Main() #Ali Mohammadi 1401\12\20