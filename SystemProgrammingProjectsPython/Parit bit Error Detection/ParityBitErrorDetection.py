def Main():
    while True:
        try:
            D = int(input("Enter the matrix dimension:"))
        except :
            print("Dimension input error.")
            continue

        matrix = []
        print("Enter the entries rowwise:")

        try:
            for i in range(D):
                a =[]
                print("Row",i+1,":")
                for j in range(D):
                     a.append(int(input()))
                matrix.append(a)
        except :
            print("Matrix input value error. Try again.")
            continue

        PrintMatrix(matrix,D)
        print(DetectError(matrix,D))
# Printing the matrix
def PrintMatrix(matrix,d):
    
    for i in range(d):
        for j in range(d):
            print(matrix[i][j], end = " ")
        print()
# Main core 
def DetectError(matrix,n):
    if(n <= 0):
        return "Invalid dimension."

    sumR = 0
    sumC = 0

    x=0 
    y = 0
    
    try:
        for i in range(0,n):
            for j in range(0,n):
               sumR += matrix[i][j]
               sumC += matrix[j][i]

            if(sumR %2 == 1): 
                if(x == 0):
                    x = i
                else:
                    return "Corrupt."
            if(sumC %2 == 1): 
                if(y == 0):
                    y = i
                else:
                    return "Corrupt."
            sumR = sumC = 0
        if(y == 0 and x == 0):
            return "Ok."
        else: 
            return "Change bit ("+str(x+1)+","+str(y+1)+")."
    except :
        return "Error calculating parity."

Main() #Ali Mohammadi