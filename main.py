import sys

import basic_op.arithmetic
import advanced_op.powering

#-----------------------
x=int(sys.argv[1])
y=int(sys.argv[3])
z=(sys.argv[2])

if (z == "+"):
    print ("The Addition is : ",basic_op.arithmetic.add(x,y))
    print ("End of the program")

elif (z == "-"):
    print ("The Substraction is : ",basic_op.arithmetic.sub(x,y))
    print ("End of the program")

elif (z == "*"):
    print ("The Multiplication is : ",basic_op.arithmetic.multi(x,y))
    print ("End of the program")

elif (z == "/"):
    print ("The Div is : ",basic_op.arithmetic.div(x,y))
    print ("End of the program")
    
elif (z == "~"):
    print ("The power value is : ",advanced_op.powering.power(x,y))
    print ("End of the program")

else:
    print ("Check your operator")
    print ("End of the program")
