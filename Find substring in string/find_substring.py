def count_substring(string, sub_string):
    sub_len = len(sub_string)
    str_len = len(string)
    count,i = 0,0
    list1 =[]
    
    while((i+sub_len) <= str_len):
        str1 =string[i:i+sub_len]
        list1.append(str1)
        i += 1
            
    for ele in list1:
        if ele == sub_string:
            count += 1

    return count

print(count_substring('ABCDCDC','CDC'))
