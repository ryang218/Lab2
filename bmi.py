def calculate_bmi(height, weight):
    print("Height = " + str(height) ,"metres")
    print("Weight = " + str(weight) , "kilograms")

    
    bmi = weight / (height * height)

    
    print(f"BMI = {bmi:.2f}" )

    
    if bmi < 18.5:
        print("Classification: Under Weight")
        return -1 
    elif 18.5 <= bmi <= 25.0:
        print("Classification: Normal Weight")
        return 0
    else:
        print("Classification: Over Weight")
        return 1 
calculate_bmi(weight=57, height=1.73)
