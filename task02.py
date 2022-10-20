import task01
def main():
    password = input("Input password:")

    result=task01.check_password(password)

    msg = f"You password is{result}" if isinstance(result, str) \
        else "User data invalid"


    print("Your password is "+ msg)

if __name__=="__main__":
    main()