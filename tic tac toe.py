def number_input():
    while True: 
        number=input("\nEnter the position you would like (1-9) : ")
        try: 
            number=int(number)
        except: 
            print("Please re enter a number between 1 and 9 : ")
            continue
        if number>=1 and number<=9:
            break
        else:
            print("Please re enter a number between 1 and 9 : ") 
    return number 
  

def move(number):
    if number<=3: 
        if board[0][number-1]=='-':
            board[0][number-1]=symbol
            info=1
        else:
            info=2
    elif number>3 and number<=6:
        if board[1][number-4]=='-':
            board[1][number-4]=symbol
            info=1
        else:
            info=2
    else:
        if board[2][number-7]=='-':
            board[2][number-7]=symbol
            info=1
        else:
            info=2
    return symbol,info       


def check_row(symbol,board):
    for i in board: 
        if i[0]==i[1] and i[0]==i[2] and i[0]==symbol:
            return True 
        else:
            pass


def check_column(symbol,board):
    if board[0][0]==board[1][0] and board[0][0]==board[2][0] and board[0][0]==symbol:
        return True 
    elif board[0][1]==board[1][1] and board[0][1]==board[2][1] and board[0][1]==symbol:
        return True
    elif board[0][2]==board[1][2] and board[0][2]==board[2][2] and board[0][2]==symbol:
        return True 
    else: 
        pass


def check_diagonal(symbol,board): 
    if board[0][0]==board[1][1] and board[0][0]==board[2][2] and board[0][0]==symbol:
        return True 
    elif board[0][2]==board[1][1] and board[0][2]==board[2][0] and board[0][2]==symbol:
        return True 
    else: 
        pass


def check():
    if check_row(symbol,board)==True or check_diagonal(symbol,board)==True or check_column(symbol,board)==True:
        return True


def check_draw(board):
    if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
        return True 


def print_board(board):
    for i in board:
        print()
        for j in i: 
            print(j,end=' ')


turn=1 
while True: 
    board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
    ]
    while True: 
        if turn%2 != 0:
            symbol='X'
        else:
            symbol='O'
        print("\n\nIt is",symbol+ "'s","turn")
        number = number_input()
        symbol,info=move(number)
        print_board(board)
        if check()==True:
            print()
            print("\n"+ symbol,"has won!")
            break
        elif check_draw(board)==True:
            print()
            print("\nIts a Draw")
            break
        else:
            if info==1:
                turn+=1
                pass
            else:
                print('\n\nThat position is occupied please enter another position')
                pass
    yes=input("\nWould you like to play again?(y/n)")
    if yes=="y":
        pass
    else:
        print("\nThank you for playing!")
        break
