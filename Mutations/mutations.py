def mutate_string(string, position, character):
    list1 = list(string)
    list1[position]=character
    output ="".join(list1)
    return output

print(mutate_string('abracadabra',5,'k'))
