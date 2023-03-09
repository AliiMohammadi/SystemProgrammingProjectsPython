#65 - 90 capital
#97 - 122 small

def Main():
    print("Welcome to this program.");
    
    while True:
        try:
            print("Enter the message:")
            messgae = input()
            print("Enter the shift value. for example : -1")
            shift = int(input())
            final = ""
            for x in messgae:
                final += EncryptChar(x,shift)
        
            print("Encrypted message:")
            print(final)
        except :
            print("Error entering input. Try again.")
            continue

        
def EncryptChar(character,shiftvalue):

    validshiftvalue = 25
    #expection for numbers above validshiftvalue or less than -validshiftvalue
    if(abs(shiftvalue) > validshiftvalue): 
        shiftvalue = shiftvalue - validshiftvalue

    keycode = ord(character)

    if (keycode >= 65) and (keycode <= 90):

        newcode = keycode + shiftvalue

        if(newcode < 65):
            newcode = 91 - (65 - newcode)
        if(newcode > 90):
            newcode = 64 + (newcode - 90)
        return chr(newcode)

    if (keycode >= 97) and (keycode <= 122):
    
        newcode = keycode + shiftvalue

        if(newcode < 97):
            newcode = 123 - (97 - newcode)
        if(newcode > 122):
            newcode = 96 + (newcode - 122)
        return chr(newcode)

    return chr(keycode)

Main() #Ali Mohammadi 1401/12/18