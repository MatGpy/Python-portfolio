'''
BMI calculator:
type your weight (in kilograms) and height (in centimetres)
'''
w = float(input("type your weight in kilograms: ")) 
h = float(input("type your height in centimetres: "))
# program does calculations necessary to calculate BMI
x = h / 100 
y = x * x
bmi = w/y
# program outputs your BMI and rates how healthy/unhealthy is your BMI
print("Your BMI is: {}".format(bmi))
if bmi <= 18:
  print("you weight too little")
if bmi > 18 and bmi <= 24:
  print("your weight is perfect")
if bmi > 24 and bmi <= 29:
  print("you weight a bit too much")
if bmi > 29 and bmi <= 35:
  print("you weight too much")
if bmi > 35:
  print("you weight way too much")