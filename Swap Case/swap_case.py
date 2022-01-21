def swap_case(s):
    string1 = ''
    for ele in s:
        if ele.isupper() == True:
            string1 += ele.lower()
        elif ele.islower() == True:
            string1 += ele.upper()
        else:
            string1 += ele
    return string1

print(swap_case('HackerRank.com presents "Pythonist 2".'))
