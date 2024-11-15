def main():
    # Prompt the user for a camelCase variable name
    camel_case = input("Enter a camelCase variable name: ")
    snake_case = convert_to_snake_case(camel_case)
    print("In snake_case:", snake_case)

def convert_to_snake_case(camel_case):
    # Initialize an empty string to build the snake_case version
    snake_case = ""
    for char in camel_case:
        # Check if the character is uppercase
        if char.isupper():
            # Add an underscore and the lowercase version of the character
            snake_case += "_" + char.lower()
        else:
            # Otherwise, add the character as it is
            snake_case += char
    return snake_case

# Run the main function
if __name__ == "__main__":
    main()
