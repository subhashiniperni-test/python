

"""for i in range(1,6):
    for j in range(1, 6):
        print("*",end='')    #  By default line ended with new line, here we define, nothing to be added at the end of line
    print()
    
    """

for i in range(1,6):
    for j in range(1, 6):
        if(i==1 or i==5):
            print("*",end='')    #  By default line ended with new line, here we define, nothing to be added at the end of line
        else:
            if(j==1 or j==5):
                print("*", end='')
            else:
                print(" ", end='')
    print()