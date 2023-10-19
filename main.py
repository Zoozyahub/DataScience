def game(num):
    a = [1, 100] # задать диопозон игре
    count = 1
    while True:
        if a[1] - a[0] <= 2:
            if num > int((a[0] + a[1])  / 2) or (a[0] == a[1] and a[1] == 1):
                a[0] = a[1]
                break         
        if num > int((a[0] + a[1])  / 2): 
            a[0] = int((a[0] + a[1])  / 2)
            count += 1
        elif num <= int((a[0] + a[1])  / 2):
            a[1] = int((a[0] + a[1])  / 2)
            count += 1
    if a[0] == num:  
        return(count)
    
print(game(1))

def test():
    for j in range(10):
        for i in range(2, 101):
            print(game(i))
        
test()