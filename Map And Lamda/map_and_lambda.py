cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    list1 = [0,1]
    for i in range(2,n):
        list1.append(list1[i-1]+list1[i-2])
    return list1[0:n]
    
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
