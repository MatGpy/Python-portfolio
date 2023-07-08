# BMI (Body Mass Index) calculator
# program takes user's input with their body weight (in kilograms) and height (in centimeters)
weight = float(input("type your weight in kilograms: ")) 
height = float(input("type your height in centimetres: "))
# program raises ValueError if values from user's input are negative
if weight < 0 or height < 0:
  raise ValueError("incorrect data in input")
# program calculates BMI value based on values from input
x = height / 100 
bmi = round(weight/(x**2), 2)
# program outputs user's BMI and an information whether their BMI is healthy, too high or too low
print("Your BMI is: {}".format(bmi))
if bmi <= 18:
  print("your weight is too low")
elif bmi > 18 and bmi <= 24:
    print("your weight is perfect")
elif bmi > 24 and bmi <= 29:
    print("your weight is a bit too high")
elif bmi > 29 and bmi <= 35:
    print("your weight is too high")
elif bmi > 35:
    print("your weight is way too high")
else:
    print("something went wrong")