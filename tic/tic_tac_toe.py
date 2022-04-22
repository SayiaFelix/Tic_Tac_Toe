'''
Creating a Dictionary with Key values:
'''

board={
   'T1' : " " ,'T2' : " ", 'T3' : " ",
   'M1' : " " ,'M2' : " ", 'M3' : " ",
   'D1' : " " ,'D2' : " ", 'D3' : " ",
}


player = 1                 #Initialize 1st players
total_moves=0              #count the moves
end_check=0                #ending the game

def check():
    #checking moives of player 1
    #for horizontal condition(START)
 if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
     print('player 1 won!!!')
     return 1

 if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
     print('player 1 won!!!')
     return 1

 if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
     print('player 1 won!!!')
     return 1

   #FOR HORIZONTAL(END)
   #for diagonal condition(start)
 if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
     print('player 1 won!!!')
     return 1
   #DIAGONAL END


   #FOR VERTICAL CONDITION(START)
 if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
     print('player 1 won!!!')
     return 1

 if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
     print('player 1 won!!!')
     return 1

 if board['T1'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
     print('player 1 won!!!')
     return 1
#FOR VERTICAL CONDYION (END)
    

    ##CHECKING MOVES OF PLAYER 2

 if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
     print('player 2 won!!!')
     return 1

 if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
     print('player 2 won!!!')
     return 1

 if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
     print('player 2 won!!!')
     return 1

   #FOR HORIZONTAL(END)
   #for diagonal condition(start)
 if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
     print('player 2 won!!!')
     return 1
   #DIAGONAL END


   #FOR VERTICAL CONDITION(START)
 if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
     print('player 2 won!!!')
     return 1

 if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
     print('player 2 won!!!')
     return 1

 if board['T1'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
     print('player 2 won!!!')
     return 1

 return 0
#FOR VERTICAL CONDYION (END)



print("\n")
name= input("Whats your Name: ")
print(f"Hello {name}, welcome at Tic Tic Toe Game Hub I Hope you will Enjoy the Game.")
print("\n")
print("Select keys from the list given: T1, D1, M1, T2, M2, D2, D3, T3, M3: To play the tic tac toe game")

# print('T1|T2|T3')
# print('-------------')
# print('M1|M2|M3')
# print('- +- +-')
# print('D1|D2|D3')
print('\n')
print('**********************************')
print(f"{name}, I Wish you Success!!!!!")
print('**********************************')
print('\n')

while True:
    print(board['T1']+ '  |  '+ board['T2'] +'  |  '+ board['T3'])
    print('-------------')
    print(board['M1']+ '  |  '+ board['M2'] +'  |  '+ board['M3'])
    print('-------------')
    print(board['D1']+ '  |  '+ board['D2'] +'  |  '+ board['D3'])

    end_check = check()
    print('\n')

    if total_moves == 9 or end_check == 1:
        break

    while True: #Taking input from players
        if player == 1: #choose player
            p1_input = input('player one')
            if p1_input.upper() in board and board[p1_input.upper()]== ' ':
                board[p1_input.upper()]= 'X'
                player = 2
                break
            #on wrong input
            else:
                print('Invalid Input, Please try again')
                continue

        else:
            p2_input = input('player two')
            if p2_input.upper() in board and board[p2_input.upper()]== ' ':
                board[p2_input.upper()]= 'O'
                player = 1
                break
            #on wrong input
            else:
                print('Invalid Input, Please try again')
                continue

    total_moves +=1
    print('****************************')
    print()
