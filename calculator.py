def main():
    number = input("enter the numbers:")
    x ,op ,y = number.split(" ")
    x = int(x)
    y = int(y)

    if op == "+":
       result = x + y
    elif op == "x-y":
        result = x-y
    elif op == "x*y":
        result = x * y
    elif op == "x/y":
        result = x / y
    elif op == "x%y":
        result=  x % y
    else:
        print("invalid")
        return
    print(f"{result:.1f}")

if __name__ == "__main__":
    main()


