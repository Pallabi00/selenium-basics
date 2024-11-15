def main():
    weight = float(input("enter your weight in kg:"))
    height = float(input("enter your height in meters:"))

    BMI = weight / (height ** 2)

    if BMI < 18.5:
        print("underweight")
    elif 18.5 <= BMI < 25 :
        print("normal")
    elif 25 <= BMI < 30:
        print("overweight")
    elif BMI >= 30:
        print("obese")
if __name__ == "__main__":
    main()




