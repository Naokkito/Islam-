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
