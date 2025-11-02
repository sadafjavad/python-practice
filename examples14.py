# Calculate Body Mass Index (BMI)
weight = 68.0 # Kg
height = 1.65 # meters
bmi = weight / (height * height)
if bmi < 18.5:
    print ("underweight")
elif bmi < 25:
    print ("normal weight")
else:
    print("overweight")
     