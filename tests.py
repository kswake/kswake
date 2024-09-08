import os
import array

# simple program demonstrating addition of 8-bit integers

bin1 = [0,1,1,0,1,0,0,1]
bin2 = [0,1,0,0,1,1,1,0]
out1 = [0,0,0,0,0,0,0,0]
carry = 0

print("bin1  |    bin2   |  result   |    carry")

for i in range (7,-1,-1): 
    
    if carry == 1:
        result = 1
        carry = 0
    else:
        if bin1[i]+bin2[i] == 2:
            carry = 1    
            result = 0
        else:
            result = bin1[i]+bin2[i]
    out1[i] = result
    
    print(str(bin1[i])+"     |     "+str(bin2[i])+"     |     "+str(result)+"     |     "+str(carry))

print(bin1)
print("     +     ")
print(bin2)
print("     =     ")
print(out1)



