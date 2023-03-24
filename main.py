
def encode(password):
    npassword=''
    for i in password:
        new_numbers=str((int(i)+3)%10)
        npassword+=new_numbers
    return npassword

def decode(password_e):
    numbers = [int(n) for n in password_e]
    new_numbers = [n - 3 for n in numbers]
    output_string = "".join([str(n) for n in new_numbers])
    return output_string

def menu():
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print('')


if __name__ == '__main__':
    r=0
    menu()
    choice=input("Please enter an option: ")
    choice=int(choice)

    while True:
        if(choice==1):
            password_i = input('Please enter your password to encode: ')
            password_e = encode(password_i)
            print('Your password has been encoded and stored!\n')
            menu()
            choice = input("Please enter an option: ")
            choice = int(choice)

        if choice==2:
            password_d=decode(password_e)
            print(f"The encoded password is {password_e}, and the original password is {password_i}.\n")
            menu()
            choice = input("\nPlease enter an option: ")
            choice = int(choice)

        if choice == 3:
            break

