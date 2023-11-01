def main():
    menu = True
    password = 0
    while menu:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")


        if option == "1":
            number = int(input("Please enter your password to encode: "))
            password = encode(number)
            print("Your password has been encoded and stored!")
            print(password)

        if option == "3":
            exit()
def encode(number): #This function encodes the inserted password adding 3 to each except when it is over 10 it returns the last digit
    output = 0
    i = 1
    while number>0:
        output += (((number%10)+3)%10)*(10**(i-1))
        i += 1
        number//= 10
    return output

if __name__ == '__main__':
    main()
