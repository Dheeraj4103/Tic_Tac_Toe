from random import randint

def check_over(mat):
    check = True    
    for itm in mat:
        if 0 in itm:
            check = False
    mat1 = []
    if not check:
        d1, d2 = [], []
        a, b = 0, 2
        for i in range(3):
            d1.append(mat[a][a])
            d2.append(mat[a][b])
            a += 1
            b -= 1
            mat1.append(mat[i])
            col = []
            for j in range(3):
                col.append(mat[j][i])
            mat1.append(col)
        mat1.append(d1)
        mat1.append(d2)
    ans = 0
    for itm in mat1:
        if 0 not in itm:
            if sum(itm) == 3:
                ans = 1
                check = True
            elif sum(itm) == 6:
                ans = 2
                check = True
    return [check, ans]
        
def Print(mat):
    symbl = {0: ' ', 1: "O", 2: "X"}
    for i in range(3):
        if i > 0:
            print("---|---|---")
        for j in range(3):
            if j < 2:
                print(" {} ".format(symbl[mat[i][j]]), end="|")
            else:
                print(" {} ".format(symbl[mat[i][j]]))


while True:
    print("0 for Exit")
    print("1 To Play")
    t = int(input())
    if t == 0:
        exit()
    mat = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = check_over(mat)
    print("You are O and computer is X")
    Print(mat)
    while(not result[0]):
        print("Your turn:- ")
        a, b = [int(itm) for itm in input().split()]
        mat[a-1][b-1] = 1
        Print(mat)
        result = check_over(mat)
        if result[0]:
            break;
        x, y = randint(0, 2), randint(0, 2)
        print("Computer's Turn")
        while(mat[x][y] > 0):
            x, y = randint(0, 2), randint(0, 2)
        mat[x][y] = 2
        Print(mat)
        result = check_over(mat)

    if (result[1] == 0):
        print("OHHH.. Match Draw")
    elif (result[1] == 1):
        print("Congratulations You Won....")
    else:
        print("Better Luck Next Time")
    Print(mat)
