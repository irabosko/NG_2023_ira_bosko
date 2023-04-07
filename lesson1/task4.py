firstcoef = int(input("write a")) 
secondcoef = int(input("write b"))
thirtcoef = int(input("write c"))
Discriminant = (secondcoef ** 2) - (4 * firstcoef * thirtcoef)
if Discriminant >=0:
    firstx = ((-secondcoef) - (Discriminant ** 0.5))/(2 * firstcoef)
    secondx = ((-secondcoef) + (Discriminant ** 0.5))/(2 * firstcoef)
    print("firstx" + str (firstcoef))
    print("secondx" + str (firstcoef))
if Discriminant == 0:
    firstx = -(secondcoef/(2 * firstcoef))
    print("answer" + str(firstcoef))
if Discriminant <=0:
    print("sorry Discriminant <0")
