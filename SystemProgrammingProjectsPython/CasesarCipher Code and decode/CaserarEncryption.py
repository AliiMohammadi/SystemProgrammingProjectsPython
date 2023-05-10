

def Main():
    print("Welcome to this program.");
    print("Amazing feature: You can enter any range shift number.");
    
    while True:
        try:
            print("Enter the message:")
            messgae = input()
            print("Enter the shift value. for example : -1")
            shift = int(input())
            final = ""
        except :
            print("Error entering input. Try again.")
            continue

        #T(x,y) = Θ(x)
        for x in messgae:
            final += EncryptChar(x,shift)

        print("Encrypted message:")
        print(final)

#Caserar Encription function:
#Parameter 1: <character> char type variable. 
#Parameter 2: <shiftvalue> integer type variable
#T(x,y) = Θ(13)
def EncryptChar(character,shiftvalue):

    keycode = ord(character)
    
    #Declaring the range of the main characters
    #65 - 90 capital letters
    #97 - 122 small letters
    CapStr = 65; CapEnd = 90
    SmaStr = 97; SmaEnd = 122

    if ((keycode >= CapStr) and (keycode <= CapEnd)) or ((keycode >= SmaStr) and (keycode <= SmaEnd)):

        validshiftvalue = 25

        #Expection for numbers above validshiftvalue or less than -validshiftvalue.
        exact = (((abs(shiftvalue) % validshiftvalue)  * shiftvalue) / abs(shiftvalue))
        
        if(exact != 0):

            newcode = int(keycode + exact)

            if (keycode >= CapStr) and (keycode <= CapEnd):
                if(newcode < CapStr):
                    newcode = (CapEnd+1) - (CapStr - newcode)
                if(newcode > CapEnd):
                    newcode = (CapStr-1) + (newcode - CapEnd)
                return chr(newcode)

            if (keycode >= SmaStr) and (keycode <= SmaEnd):
                if(newcode < SmaStr):
                    newcode = (SmaEnd+1) - (SmaStr - newcode)
                if(newcode > SmaEnd):
                    newcode = (SmaStr-1) + (newcode - SmaEnd)
                return chr(newcode)

    return chr(keycode)

Main() #Ali Mohammadi 1401/12/18