import random

grid=[["_","_","_"],["_","_","_"],["_","_","_"]]
def result(grid,p,c): #player won=1,computer won=-1,draw=0,not over=99
    for row in grid:
        if row[0]==row[1] and row[1]==row[2]:
            if row[0]==p:
                return 1
            elif row[0]==c:
                return -1 #next line
    i = 0

    while i < 3:
        if grid[0][i]==grid[1][i] and grid[2][i]==grid[1][i]:
            if grid[0][i]==p:
                return 1
            elif grid[0][i]==c:
                return -1
        i = i + 1
    i=0
    j=0
    count=0
    while i < 3:
        while j < 3:
            if grid[i][j]!="_":
                count=count+1
            j=j+1
        i=i+1
    if count==9:
        return 0
    if grid[0][0]==grid[1][1] and grid[1][1]==grid[2][2]:
        if grid[1][1]==p:
            return 1
        elif grid[1][1]==c:
            return -1
    if grid[0][2]==grid[1][1] and grid[2][0]==grid[1][1]:
        if grid[1][1]==p:
            return 1
        elif grid[1][1]==c:
            return -1
    return 99


def displayResult(grid,p,c):
    if result(grid,p,c)==1:
        print("player won")
    elif result(grid,p,c)==-1:
        print("computer won")
    elif result(grid,p,c)==0:
        print("Its a draw")
    elif result(grid,p,c)==99:
        print("game continues")
    else:
        print("something's wrong")


def display(grid):
    for row in grid:
        print(str(row[0])+" "+str(row[1])+" "+str(row[2]))

def compTurn(grid,p,c):
    while True:
        i=random.randint(0,2)
        j=random.randint(0,2)
        if grid[i][j]=="_":
            grid[i][j]=c
            break
    return grid


def playerTurn(grid,p,c):
    while True:
        print("Your turn")
        row=int(input("Enter row (1 to 3): "))-1
        col=int(input("Enter column (1 to 3): "))-1
        if grid[row][col]!="_":
            print("That's already marked, choose other location!")
            continue
        grid[row][col]=p
        break
    return grid

while True:
    p=input("Enter player character(x or o): ")
    if p=="x":
        c="o"
        break
    elif p=="o":
        c="x"
        break
    print("Enter either x or o only!")
x=int(input("Wanna go first or second ?: "))
k=1
while True:
    print("\n")
    if k%2==x%2:
        display(grid)
        grid=playerTurn(grid,p,c)
    else:
       grid=compTurn(grid,p,c)
    if result(grid,p,c)!=99:
        displayResult(grid,p,c)
        break
    k=k+1
print("Final grid:")
display(grid)

