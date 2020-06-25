#divisible by 5 and 11 both

i=input("enter number")

if(int(i)%5==0 and int(i)%11==0):
    print(i+" divided by both numbers 5 and 11")
elif(int(i)%5==0):
    print(i + " divided by only 5 ")
elif (int(i)%11==0):
    print(i + " divided by only 11 ")
else:
     print(i + " not divided by numbers 5 or 11")
