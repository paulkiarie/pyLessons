# ---Creating a file to calculate BMI ----- #
# ----INVOLVES WEIGHT(KG) DIVIDED BY HEIGHT(M)SQUIRED --- #

# enter inputs from cmd and output the result
name_of_guy = str(input('Please enter your name'))                   # object of class string
weight = float(input('Enter  your weight'))                          # object of class float
height = float(input('Enter your height'))                           # object of classn float

# function to calculate bmi
def bmi():
    bmi = weight / (height * height)
    print("Dear", name_of_guy, "Your BMI is ", bmi)
    if bmi < 17:
        print("You are underweight")
    elif bmi < 22:
        print("Normal BMI")
    elif bmi < 28:
        print("Much heavy: Regular exercises required")
    else:
        print("you are over weight")

#call the bmi function here
bmi_result = bmi()

