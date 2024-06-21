year = int(input("enter the year number:"))
if year%100==0 :
    if year%400==0:
         print(" leap year")
    else :
        print("nrml year")
elif year%4==0:
    print("leap year")
else :
    print("nrml year")
