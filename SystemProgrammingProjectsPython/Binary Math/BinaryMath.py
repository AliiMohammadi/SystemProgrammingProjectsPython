import RegisterFlags

def BinarySum(a, b):
    carry = 0
    result = ""

    # Make sure both strings have the same length by adding leading zeros
    if len(a) > len(b):
        b = "0" * (len(a) - len(b)) + b
    else:
        a = "0" * (len(b) - len(a)) + a

    # Iterate through the strings from right to left
    for i in range(len(a)-1, -1, -1):
        # Calculate the sum of the current digits and the carry
        s = int(a[i]) + int(b[i]) + carry

        # If the sum is 2 or 3, set the carry to 1
        if s == 2 or s == 3:
            carry = 1
        else:
            carry = 0

        # Append the result to the output string
        result = str(s % 2) + result

    # If there's still a carry left over, add it to the beginning of the output string
    if carry == 1:
        result = "1" + result

    return result

