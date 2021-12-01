def All_uppercase(s):
    result = ''
    for char in s:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
s = input("Enter something in lower case:")
print(All_uppercase(s))