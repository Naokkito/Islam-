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
