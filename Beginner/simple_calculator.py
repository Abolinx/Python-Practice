
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiple(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "ERROR: CANNOT DIVIDE BY ZERO!"
    return x / y

def calculator_menu():
    print("____WELLCOME TO SIMPLE CALCULATOR____\n")
    print("1. ADD(+)")
    print("2. SUBTRACT(-)")
    print("3. MULTPLE(×)")
    print("4. DIVIDE(÷)")
    print("5. EXIT")
    
    while True:
        choice = input("PLEASE CHOOSE YOUR OPERATION(1,2,3,4,5):")

        if choice == "5":
            print("BYE BYE👋")
            break
        
        if choice in ("1", "2", "3", "4"):
            
            try:
                num1 = float(input("FIRST NUMBER:"))
                num2 = float(input("SECOND NUMBER:"))
            except ValueError:
                print("INVALID INPUT PLEASE ENTER A NUMBER.❌")
                continue
            
            if choice == "1":
                print(f"RESULT: {num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"RESULT: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"RESULT: {num1} × {num2} = {multiple(num1, num2)}")
            elif choice == "4":
                res = divide(num1, num2)
                print(f"RESULT: {num1} ÷ {num2} = {res}")
        else:
            print("INVALID SELECTION; PLEASE USE NUMBERS 1 TO 5.❌")

if __name__ == "__main__":
    calculator_menu()