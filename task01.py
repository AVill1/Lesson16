import string
def check_password(password):

    if (not isinstance(password, str)
        or len(password.strip())==0):
        return -1

    password = password.strip()
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    if len(password)<8:
        return"too weak"

    #is_digit = True
    if  (all(ch  in digit for ch in password)
        or all([ch  in lower for ch in password])
        or all([ch  in upper for ch in password])):
    # for ch in password:
    #     if ch not in DIGITS:
    #         is_digit = False
    #         break
    #
    # is_lower = True
    # for ch in password:
    #     if ch not in LOWER_CASE:
    #         is_lower = False
    #         break
    #
    # is_upper = True
    # for ch in password:
    #     if ch not in UPPER_CASE:
    #         is_upper = False
    #         break
    # if is_upper or is_lower or is_digit:
        return "weak"

    # is_digit = False
    # for ch in password:
    #    if ch in DIGITS:
    #         is_digit=True
    #         break
    # is_lower = False
    # for ch in password:
    #    if ch in LOWER_CASE:
    #         is_lower = True
    #         break
    # is_upper = False
    # for ch in password:
    #    if ch in UPPER_CASE:
    #        is_upper = True
    #        break
    # if is_upper and is_lower and is_digit:
    if (any(ch in digit for ch in password)
        and any([ch in lower for ch in password])
        and any([ch in upper for ch in password])):
        return "very strong"

    return "strong"


   # password=input("Enter password:")
    #result=0
    #if len(password) < 8:
        #result = "too weak"

    #elif 3 >= mark >= 2:
        #result = "weak"
    #elif mark == 4:
        #result = "strong"
    #elif 6 >= mark >= 5:
        #result = "very strong"
    #elif 8 >= mark >= 7:
       # result = "Unacceptable"
    #return result

if __name__=="__main__":
    assert check_password("") == -1
    assert check_password(" ") == -1
    #assert check_password(",#$%><'") == "Unacceptable"
    assert check_password(None) == -1
    assert check_password(10) == -1
    assert check_password(10.5) == -1
    assert check_password([1,2,3,4,5,6]) == -1

    assert check_password("123") == "too weak"
    assert check_password("qwe") == "too weak"
    assert check_password("QWE") == "too weak"
    assert check_password("1Qe") == "too weak"

    assert check_password("12345678") == "weak"
    assert check_password("QQQQQQQQ") == "weak"
    assert check_password("qqqqqqqq") == "weak"
    assert check_password("123456789") == "weak"
    assert check_password("sekdithropenn") == "weak"

    assert check_password("11111AAAAA") == "strong"
    assert check_password("11111aaaaaaa") == "strong"
    assert check_password("aaaaaAAAAA") == "strong"

    assert check_password("11AAaaaa") == "very strong"
    assert check_password("11AAaaaaA") == "very strong"


    assert check_password("11111AAAAA") == "strong"
    assert check_password("11111aaaaaaa") == "strong"
    assert check_password("aaaaaAAAAA") == "strong"





