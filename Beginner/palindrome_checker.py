import re

def palindrome_cheker(string):
    string = re.sub(r'[^a-zA-Z0-9]','',string).lower()
    return (string == string[::-1])

def main():

    print("___welcome to palindrome cheker___")

    while True:
        
        user_input = input("enter your word (or type 'exit')")
        
        if user_input.lower() == 'exit':
            print("Bye Bye👋")
            break

        if ((user_input != user_input.strip())) or len(user_input.strip().replace(" ","")) <= 2:
            print("please enter valid input")
            continue

        if palindrome_cheker(user_input):
            print(f"Yes, {user_input} is a palindrome")
        
        else:
            print(f"No, {user_input} is not a palindrome")

if __name__ == "__main__":
    main()
