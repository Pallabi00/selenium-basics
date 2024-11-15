from indoor import user_input


def convert(input_str):
 output_str = input_str.replace(":)", "🙂")
 output_str = output_str.replace(":(", "🙁")
 return output_str

def main():
 user_input = input("enter text with :) or :( :")
 print(convert(user_input))

if __name__ == "__main__":
    main()
