def swap_case(s):
    b = ""
    for let in s:
        if let.isupper() == True:
            b+=(let.lower())
        else:
            b+=(let.upper())
    return b
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
