if __name__ == '__main__':
    entry = int(input())
    records = []
    score_list = []
    final = []
    for _ in range(entry):
        name = input()
        score = float(input())
        list1 = [name,score]
        score_list.append(score)
        records.append(list1)
        
    s = set(score_list)
    sorted_list = sorted(s)
    sec_min = sorted_list[1]
    
    for i in range(len(records)):
        if records[i][1] == sec_min:
            final.append(records[i][0])
    
    final.sort()
    for element in final:
        print(element)
