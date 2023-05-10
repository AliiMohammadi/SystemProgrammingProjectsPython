import decimal
import time

#1
def FlooredTest():
    print(5//2)
#2
def BinTest():
    a = 6
    print(bin(a))#0bNUMBER
#3
def DecimalTest():
    a = decimal.Decimal('0.6')
    b = decimal.Decimal('0.2')
    print(a == (b+b+b))

def HexTest():
    a = 20
    print(hex(a))#0xNUMBER

def OctTest():
    a = 20 
    print(oct(a)) #0oNUMBER

def CharToValue():
    a = ord('A')
    b = chr(65)
    print(a,b)
    
def Exponential():
    a = 22E2
    print(a)

def ListValue():
    a = "HELLO WORLD"
    print([ord(c) for c in a])

def DivZero():
    try:
        a = 4 / 0
        print(a)
    except ZeroDivisionError:
       print("Error: Imposible operation.")

def Intruption():
    for x in range(0,10):
        time.sleep(1)
        print(x+1)
    
Intruption()