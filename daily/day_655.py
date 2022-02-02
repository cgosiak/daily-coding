def reverseBits(n) :
    rev = 0
    # traversing bits of 'n' from the right
    while (n > 0) :
         
        # bitwise left shift 'rev' by 1
        rev = rev << 1
         
        # if current bit is '1'
        if (n & 1 == 1) :
            rev = rev ^ 1
         
        # bitwise right shift 'n' by 1
        n = n >> 1
         
     
    # required number
    return rev
     
# Driver code
n = 10
print(reverseBits(n))

# 10 -> 1010
# 5 -> 101
# 3 -> 11
# 6 -> 110

test = 3
test = test ^ 1
print(test)