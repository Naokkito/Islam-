try:
    x = int(input("enter score:"))
    if x >= 90:
        print("A", end= "")
    else:
        if x >= 80:
            print("B", end="")
        else:
            if x >= 70:
                print("C", end= " ")
            else:
                if x >= 60:
                    print("D", end="")
                else:
                    print("F", end="")
    print("grade")
except:
    print("Error, please enter numeric input between 0 and 100")

    /////////////////////////


try:
   hours = int(input("enter hours:"))
   rate = int(input("enter rate:"))
   salary = hours*rate
   if hours < 40:
       print(salary)
   else:
        if hours >= 40:
            print((40*rate) + ((hours%40)*1.5)*10)
except:
    print("Error, please enter numeric")

///////////////////////////

sum = 0
num = 0

while True:
    input_u = input("enter sa number:")
    if input_u == "done":
        break
    try:
        c = int(input_u)
        sum += c
        num += 1
    except:
        print("invalid input. enter a number")
if num > 0:
    c = sum / num
    print("Sum:" + str(sum))
    print("Count:" + str(num))
    print("Average:" + str(c))























