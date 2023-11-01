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

        if option == "2":
            decoded = decode(password)
            print(f"The decoded password is {decoded}, and the original password is {password}")

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

def decode(num):
    result = 0
    i = 0
    while num>0:
        temp = (num%10)-3
        if temp == -1:
            temp = 9
        if temp == -2:
            temp = 8
        if temp == -3:
            temp = 7
        result += temp*(10**i)
        i += 1
        num //= 10
    return result


if __name__ == '__main__':
    main()
