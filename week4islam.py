def calculate_grade(score):
  if score < 0 or score > 100:
    return "Error, please enter numeric input between 0 and 100"
  else:
      if score >= 90:
        return "A"
      else:
          if score >= 80:
            return "B"
          else:
              if score >= 70:
                return "C"
              else:
                if score >= 60:
                  return "D"
                else:
                  if score >= 50:
                    return "F"
try:
  score = int(input("enter your grade:"))
  grade = calculate_grade(score)
  print(f"Grade: {grade}")
except:
  print("Error, please enter numeric input between 0 and 100")

  ////////////////

def overal_salary(hours, rate):
    if hours > 40:
        over_hours = (40*rate) + ((hours%40)*1.5)*10
        return over_hours
    elif hours <= 40:
        salary_40 = hours * rate
        return salary_40
try:
    hours = int(input("enter hours:"))
    rate = int(input("enter rate:"))
    pay = overal_salary(hours, rate)
    print(f"salary:", pay)
except:
    print("Error: Please enter valid numeric values for hours and rate.")

    ///////////////////

def num_divide3(a):
    num = 0
    for i in range(1, a + 1):
        if i % 3 == 0:
            num = num + 1
    return num
while True:
    input_number = (input("Enter a positive integer:"))
    if input_number == "done":
        print("bye!!")
        break
    try:
        c = int(input_number)
        if c < 1:
            print("enter a positive number")
        else:
            result = num_divide3(c)
            print(f"The number of numbers divisible by 3 from 1 to {c} is {result}.")
    except:
        print("please enter a positive number")