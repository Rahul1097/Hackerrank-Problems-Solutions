if __name__ == '__main__':
    list1 = []
    N = int(input())
    for i in range(N):
        command,*numbers = input().split()
        
        if command == 'insert':
            list1.insert(int(numbers[0]),int(numbers[1]))
            
        elif command == 'print':
            print(list1)
            
        elif command == 'remove':
            list1.remove(int(numbers[0]))
        
        elif command == 'append':
            list1.append(int(numbers[0]))
        
        elif command == 'sort':
            list1.sort()
        
        elif command == 'pop':
            list1.pop()
        
        elif command == 'reverse':
            list1.reverse()
            
